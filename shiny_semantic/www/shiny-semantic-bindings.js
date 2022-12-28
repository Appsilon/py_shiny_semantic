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
    // TODO(pavel): this initialize does not match the original R/Shiny binding
    // and it will not work with custom ticks, e.g. letters
    const {
      min,
      max,
      start,
      step,
      end,
      showlabelticks: showLabelTicks,
    } = $(el).data();

    const onChange = (_value) => $(el).trigger("change");

    $(el).slider({ min, max, start, step, end, showLabelTicks, onChange });
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
