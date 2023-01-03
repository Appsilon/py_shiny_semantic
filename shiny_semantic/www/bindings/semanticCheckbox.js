// compared to shiny.semantic: new implementation

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

export default semanticCheckboxBinding;
