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
Shiny.addCustomMessageHandler("showSemanticModal", (payload) => {
  const modalId = $(payload.ui).attr("id");
  const modalProps = payload.props ?? {};

  // Gotta remove all modals with this id - otherwise they accumulate in the DOM
  $(`[id=${modalId}]`).remove();

  console.log(payload.shiny_input);

  $(payload.ui)
    .modal({
      ...modalProps,
      onDeny: () => Shiny.setInputValue(payload.shiny_input, false),
      onApprove: () => Shiny.setInputValue(payload.shiny_input, true),
    })
    .modal("show");
});

var semanticDropdownBinding = new Shiny.InputBinding();

$.extend(semanticDropdownBinding, {
  // This initialize input element. It extracts data-value attribute and use that as value.
  initialize: function (el) {
    $(el).dropdown();
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
