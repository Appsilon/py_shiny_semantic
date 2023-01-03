/**
 * All shiny <-> semantic bindings in one file
 * to be loaded when the app first loads
 *
 * The code below was originally developed by Appsilon team for `shiny.semantic` R package
 * https://github.com/Appsilon/shiny.semantic
 */

import semanticButtonBinding from "./bindings/semanticButton.js";
import semanticCheckboxBinding from "./bindings/semanticCheckbox.js";
import semanticCheckboxGroupBinding from "./bindings/semanticCheckboxGroup.js";
import semanticDropdownBinding from "./bindings/semanticDropdown.js";
import showSemanticModal from "./bindings/semanticModal.js";
import semanticSliderBinding from "./bindings/semanticSlider.js";

Shiny.inputBindings.register(semanticButtonBinding, "shiny.semanticButton");
Shiny.inputBindings.register(semanticSliderBinding, "shiny.semanticSlider");
Shiny.inputBindings.register(semanticDropdownBinding, "shiny.semanticDropdown");
Shiny.inputBindings.register(semanticCheckboxBinding, "shiny.semanticCheckbox");
Shiny.inputBindings.register(
  semanticCheckboxGroupBinding,
  "shiny.semanticCheckboxGroup",
);

// Modal dialog is invoked via session.send_custom_message()
$.fn.modal.settings.onShow = () => Shiny.bindAll();
Shiny.addCustomMessageHandler("showSemanticModal", showSemanticModal);
