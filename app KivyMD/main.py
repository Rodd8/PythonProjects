from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.toolbar import MDToolbar
from kivymd.icon_definitions import md_icons
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield.textfield import MDTextField


class IMCApp(MDApp):
    def calcul_IMC(self, args) -> None:
        self.weightTextField.text = self.weightTextField.text.replace(',','.')
        self.heightTextField.text = self.heightTextField.text.replace(',','.')
        
        try:
            weight = float(self.weightTextField.text)
            height = float(self.heightTextField.text)
            imc = round(weight / (height**2), 2)
            comment = ""
            if imc < 18.5:
                comment = "Insuffisance pondérale"
            elif imc < 25:
                comment = "Corpulence normale"
            elif imc < 30:
                comment = "Surpoids"
            elif imc < 35:
                comment = "Obésité modérée"
            elif imc < 40:
                comment = "Obésité sévère"
            else:
                comment = "Obésité morbide"
                
            self.labelIMC.text = f"Votre IMC est de : {str(imc)}\n {comment}"
        except:
            pass
    
    
    def resetFields(self) -> None:
        self.weightTextField.text = ""
        self.heightTextField.text = ""
        self.labelIMC.text = "Remplissez les champs et cliquez sur le bouton ;)"
    
    
    def build(self):
        screen = Screen()
        
        # Top Toolbar
        self.toolbar = MDToolbar(title="Calcultateur d'IMC")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items= [
            ["rotate-3d-variant", lambda _: self.resetFields()]
        ]
        screen.add_widget(self.toolbar)
        
        # Bouton calculer IMC
        self.calculateIMCButton = MDFillRoundFlatButton(
            text="Calculer mon IMC...",
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            on_press=self.calcul_IMC
        )
        screen.add_widget(self.calculateIMCButton)
        
        # champ de texte poids
        self.weightTextField = MDTextField(
            hint_text="Entrer votre poids (kg)",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            icon_right="scale",
            required = True,
            size_hint = (.8, 1)
        )
        screen.add_widget(self.weightTextField)
        
        # champ de texte taille
        self.heightTextField = MDTextField(
            hint_text="Entrer votre taille (m)",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            icon_right="arrow-expand-vertical",
            required = True,
            size_hint = (.8, 1)
        )
        screen.add_widget(self.heightTextField)
        
        # label résultat IMC
        self.labelIMC = MDLabel(
            text="Remplissez les champs et cliquez sur le bouton ;)",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            halign="center",
            size_hint =(.8, 1)
        )
        screen.add_widget(self.labelIMC)
        
        return screen


IMCApp().run()