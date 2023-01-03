// compared to shiny.semantic: new implementation

const semanticCheckboxGroupBinding = new Shiny.InputBinding();

$.extend(semanticCheckboxGroupBinding, {
  initialize: (el) => $(el).checkbox({ fireOnInit: true }),
  find: (scope) => $(scope).find(".ss-checkbox-group"),
  getId: (el) => el.id,
  getValue: (el) => {
    const selected = $(el)
      .find(".ui.checkbox")
      .filter((_idx, e) => $(e).checkbox("is checked"))
      .map((_idx, e) => $(e).data("shinyValue"))
      .toArray();

    // Handle radio buttons return value differently
    const isRadioGroup = $(el).find(".radio").length > 0;
    if (isRadioGroup) return selected[0];

    return selected;
  },
  setValue: (el, values) => {
    const checkboxes = $(el).find(".ui.checkbox");
    $.each(checkboxes, (idx, item) => $(item).checkbox(values[idx] ? "check" : "uncheck"));
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

export default semanticCheckboxGroupBinding;
