/**
 * All shiny <-> semantic bindings in one file
 * to be loaded when the app first loads
 *
 * The code below was originally developed by Appsilon team for `shiny.semantic` R package
 * https://github.com/Appsilon/shiny.semantic
 */

var semanticButtonBinding = new Shiny.InputBinding();
$.extend(semanticButtonBinding, {
  find: function (scope) {
    return $(scope).find(".button");
  },
  getValue: function (el) {
    return $(el).data("val") || 0;
  },
  setValue: function (el, value) {
    $(el).data("val", value);
  },
  getType: function (el) {
    return "shiny.action";
  },
  subscribe: function (el, callback) {
    $(el).on("click.semanticButtonBinding", function (e) {
      var $el = $(this);
      var val = $el.data("val") || 0;
      $el.data("val", val + 1);

      callback();
    });
  },
  getState: function (el) {
    return { value: this.getValue(el) };
  },
  receiveMessage: function (el, data) {
    var $el = $(el);
    // retrieve current label and icon
    var label = $el.text();
    var icon = "";

    // to check (and store) the previous icon, we look for a $el child
    // object that has an i tag, and some (any) class (this prevents
    // italicized text - which has an i tag but, usually, no class -
    // from being mistakenly selected)
    if ($el.find("i[class]").length > 0) {
      var icon_html = $el.find("i[class]")[0];
      if (icon_html === $el.children()[0]) {
        // another check for robustness
        icon = $(icon_html).prop("outerHTML");
      }
    }

    // update the requested properties
    if (data.hasOwnProperty("label")) label = data.label;
    if (data.hasOwnProperty("icon")) {
      icon = data.icon;
      // if the user entered icon=character(0), remove the icon
      if (icon.length === 0) icon = "";
    }

    // produce new html
    $el.html(icon + " " + label);
  },
  unsubscribe: function (el) {
    $(el).off(".semanticButtonBinding");
  },
});
Shiny.inputBindings.register(semanticButtonBinding, "shiny.semanticButton");

/**
 * Semantic Modal Dialog
 * NOTE: the code for Modal Dialog is mostyle re-implemented.
 */
$.fn.modal.settings.onShow = () => Shiny.bindAll();

Shiny.addCustomMessageHandler("showSemanticModal", (payload) => {
  const modalId = $(payload.ui).attr("id");
  const modalProps = payload.props ?? {};

  const $modal = $(`#${modalId}`);

  // First time: create the modal based on UI provided in the payload
  if ($modal.length === 0) {
    $(payload.ui)
      .modal({
        ...modalProps,
        onDeny: () => Shiny.setInputValue(payload.shiny_input, false),
        onApprove: () => Shiny.setInputValue(payload.shiny_input, true),
      })
      .modal("show");
    return;
  }

  // Not first time: find existing modal and invoke it
  $modal.modal("show");
});

/**
 * Semantic slider binding
 */
var semanticSliderBinding = new Shiny.InputBinding();

$.extend(semanticSliderBinding, {
  // This initialize input element. It extracts data-value attribute and use that as value.
  initialize: function (el) {
    const { min, max, start, step, end, labels } = $(el).data();
    const onChange = (_value) => $(el).trigger("change");

    let interpretLabel = undefined;
    if (!!labels) {
      interpretLabel = (value) => labels[value];
    }

    $(el).slider({ min, max, start, step, end, onChange, interpretLabel });
  },

  // This returns a jQuery object with the DOM element.
  find: function (scope) {
    // checkbox with type slider was also found here causing: https://github.com/Appsilon/shiny.semantic/issues/229
    return $(scope).find(".ss-slider");
  },

  // Returns the ID of the DOM element.
  getId: function (el) {
    return el.id;
  },

  // Given the DOM element for the input, return the value as JSON.
  getValue: function (el) {
    let value = $(el).slider("get value");
    // Takes either one or two arguments depending on if it's a range or normal slider
    if ($(el).hasClass("range")) {
      value = [
        $(el).slider("get thumbValue", "first"),
        $(el).slider("get thumbValue", "second"),
      ];
    }

    if ($(el).data("ticks")) {
      return $(el).data("ticks")[value];
    } else {
      return value;
    }
  },
  getType: function (el) {
    if ($(el).data("ticks")) {
      return false;
    } else {
      return "shiny.number";
    }
  },
  // Given the DOM element for the input, set the value.
  setValue: function (el, value) {
    if ($(el).data("ticks")) {
      if ($(el).hasClass("range")) {
        $(el).slider(
          "set rangeValue",
          $(el).data("ticks").indexOf(value[0]),
          $(el).data("ticks").indexOf(value[1]),
        );
      } else {
        $(el).slider("set value", $(el).data("ticks").indexOf(value[0]));
      }
    } else {
      if ($(el).hasClass("range")) {
        $(el).slider("set rangeValue", value[0], value[1]);
      } else {
        $(el).slider("set value", value[0]);
      }
    }
  },

  // Set up the event listeners so that interactions with the
  // input will result in data being sent to server.
  // callback is a function that queues data to be sent to
  // the server.
  subscribe: function (el, callback) {
    $(el).on("keyup change", function () {
      callback(true);
    });
  },

  // TODO: Remove the event listeners.
  unsubscribe: function (el) {
    $(el).off(".semanticSliderBinding");
  },

  // This returns a full description of the input's state.
  getState: function (el) {
    return {
      value: this.getValue(el),
    };
  },

  // The input rate limiting policy.
  getRatePolicy: function () {
    return {
      // Can be 'debounce' or 'throttle':
      policy: "debounce",
      delay: 50,
    };
  },

  receiveMessage: function (el, data) {
    if (data.hasOwnProperty("value")) {
      this.setValue(el, data.value);
    }

    $(el).trigger("change");
  },
});

Shiny.inputBindings.register(semanticSliderBinding, "shiny.semanticSlider");

/**
 * Semantic dropdown selection
 * NOTE: all code in this section is copy-pasted from shiny.semantic,
 * except for `initialize` method - it was re-implementd.
 */

var semanticDropdownBinding = new Shiny.InputBinding();

$.extend(semanticDropdownBinding, {
  initialize: function (el) {
    const settings = JSON.parse(el.dataset.settings);
    $(el).dropdown({ ...settings });
  },

  // This returns a jQuery object with the DOM element.
  find: function (scope) {
    return $(scope).find(".semantic-select-input");
  },

  // Returns the ID of the DOM element.
  getId: function (el) {
    return el.id;
  },

  // Given the DOM element for the input, return the value as JSON.
  getValue: function (el) {
    let value = $(el).dropdown("get value");
    // Enables the dropdown to be a vector if multiple class
    if ($(el).hasClass("multiple")) {
      if (value === "") {
        return null;
      }
      value = value.split(",");
    }
    return value;
  },

  // Given the DOM element for the input, set the value.
  setValue: function (el, value) {
    if ($(el).hasClass("multiple")) {
      $(el).dropdown("clear", true);
      value.split(",").map((v) => $(el).dropdown("set selected", v));
    } else {
      $(el).dropdown("set selected", value);
    }
  },

  // Set up the event listeners so that interactions with the
  // input will result in data being sent to server.
  // callback is a function that queues data to be sent to
  // the server.
  subscribe: function (el, callback) {
    $(el).dropdown({
      onChange: function () {
        callback();
        $(el).dropdown("hide");
      },
    });
  },

  // TODO: Remove the event listeners.
  unsubscribe: function (el) {
    $(el).off();
  },

  receiveMessage: function (el, data) {
    if (data.hasOwnProperty("choices")) {
      // setup menu changes dropdown options without triggering onChange event
      $(el).dropdown("setup menu", data.choices);
      // when no value passed, return null for multiple dropdown and first value for single one
      if (!data.hasOwnProperty("value")) {
        let value = "";
        if (!$(el).hasClass("multiple")) {
          value = data.choices.values[0].value;
        }
        this.setValue(el, value);
      }
    }

    if (data.hasOwnProperty("value")) {
      this.setValue(el, data.value);
    }

    if (data.hasOwnProperty("label")) {
      $("label[for='" + el.id + "'").html(data.label);
    }
  },
});

Shiny.inputBindings.register(semanticDropdownBinding, "shiny.semanticDropdown");

/**
 * Semantic checkbox binding
 * NOTE (PD): I took the original binding, split it into two:
 * checkbox and checkboxGroup to be separate,
 * and modified the code to some extent.
 */
const semanticCheckboxBinding = new Shiny.InputBinding();
$.extend(semanticCheckboxBinding, {
  initialize: (el) => $(el).checkbox({ fireOnInit: true }),
  find: (scope) => $(scope).find(".ui.checkbox"),
  getId: (el) => el.id,
  getValue: (el) => $(el).checkbox("is checked"),
  setValue: (el, val) => $(el).checkbox(val ? "check" : "uncheck"),
  subscribe: (el, callback) => $(el).checkbox({ onChange: () => callback() }),
  unsubscribe: (el) => $(el).off(),
  receiveMessage: function (el, data) {
    const { value, label } = data;
    if (value !== undefined) this.setValue(el, value);
    if (label !== undefined) $(`label[for='${el.id}']`).html(label);
  },
});

Shiny.inputBindings.register(semanticCheckboxBinding, "shiny.semanticCheckbox");

const semanticCheckboxGroupBinding = new Shiny.InputBinding();

$.extend(semanticCheckboxGroupBinding, {
  initialize: (el) => $(el).checkbox({ fireOnInit: true }),
  find: (scope) => $(scope).find(".ss-checkbox-group"),
  getId: (el) => el.id,
  getValue: (el) => {
    const selected = $(el)
      .find(".ui.checkbox")
      .filter((_idx, e) => $(e).checkbox("is checked"))
      .map((_idx, e) => $(e).find("label").text())
      .toArray();

    // Handle radio buttons return value differently
    const isRadioGroup = $(el).find(".radio").length > 0;
    if (isRadioGroup) return selected[0];

    return selected;
  },
  setValue: (el, values) => {
    const checkboxes = $(el).find(".ui.checkbox");
    $.each(checkboxes, (idx, item) =>
      $(item).checkbox(values[idx] ? "check" : "uncheck"),
    );
  },
  setLabels: (el, labels) => {
    const checkboxes = $(el).find(".ui.checkbox");
    $.each(checkboxes, (idx, item) => {
      $(item)
        .find("label[for='" + item.querySelector("input").id + "'")
        .html(labels[idx]);
    });
  },
  setGroupLabel: (el, label) => $(el).find("label").first().html(label),
  subscribe: (el, callback) => $(el).checkbox({ onChange: () => callback() }),
  unsubscribe: (el) => $(el).off(),
  receiveMessage: function (el, data) {
    const { values, labels, group_label } = data;
    if (values !== undefined) this.setValue(el, values);
    if (labels !== undefined) this.setLabels(el, labels);
    if (group_label !== undefined) this.setGroupLabel(el, group_label);
  },
});

Shiny.inputBindings.register(
  semanticCheckboxGroupBinding,
  "shiny.semanticCheckboxGroup",
);
