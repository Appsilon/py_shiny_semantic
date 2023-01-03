// compared to shiny.semantic: new implementation

const showSemanticModal = (payload) => {
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
};

export default showSemanticModal;
