from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.layout import Layout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from math import sin, cos, tan, sqrt, asin, acos, atan, degrees, radians


def convert_float(x):
    my_num = x
    try:
        return float(x)
    except ValueError as e:
        try:
            for i in range(len(x[::-1])):
                if x[i].isalpha():
                    my_num = x[:i]
            return float(my_num)
        except ValueError as e:
            return ""


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.box_height = "100dp"
        self.text_size = "32dp"
        self.btn_radius = [10]

class VertForce(Screen):
    def __init__(self, **kwargs):
        super(VertForce, self).__init__(**kwargs)
        
    def calculate(self):
        """Pulls text input from kivy form for VertForce screen.  Checks for minimum inputs and calculates Newtons and Degrees"""
        self.vertical_force_y = convert_float(self.ids.vertical_force_y.text)
        self.vertical_force = convert_float(self.ids.vertical_force.text)
        self.vertical_force_angle = convert_float(self.ids.vertical_force_angle.text)
        self.vertical_force_sin_angle = convert_float(self.ids.vertical_force_sin_angle.text)

        #One way or another the sin(angle) will be produced for use later
        if self.vertical_force_sin_angle == "" and self.vertical_force_angle != "":
            self.vertical_force_sin_angle = sin(radians(self.vertical_force_angle))
            self.ids.vertical_force_sin_angle.text = str(f"{self.vertical_force_sin_angle:,.6f}")

        elif self.vertical_force_sin_angle != "" and self.vertical_force_angle == "":
            self.ids.vertical_force_angle.text = str(f"{degrees(asin(self.vertical_force_sin_angle)):,.6f}")

        elif self.vertical_force_sin_angle != "" and self.vertical_force_angle != "":
            if str(f'{degrees(asin(self.vertical_force_sin_angle)):,.2f}') != str(f'{self.vertical_force_angle:,.2f}'):
                error_popup = Popup(title='Check values!', content=Label(text='sin(angle) and angle don\'t match'), size_hint=(0.7, 0.7))
                error_popup.open()
            #self.ids.vertical_force_sin_angle.text = str(f"{self.vertical_force_sin_angle:,.6f}")
            #self.ids.vertical_force_angle.text = str(f"{self.vertical_force_angle:,.6f}")

        elif self.vertical_force_y != "" and self.vertical_force != "":
            self.vertical_force_sin_angle = float(self.vertical_force_y) / float(self.vertical_force)
            self.ids.vertical_force_sin_angle.text = str(f"{self.vertical_force_sin_angle:,.6f}")
            self.ids.vertical_force_angle.text = str(f"{degrees(asin(self.vertical_force_sin_angle)):,.6f}")
            
        else:
            error_popup = Popup(title='Need more info!', content=Label(text='Not enough values to complete'), size_hint=(0.7, 0.7))
            error_popup.open()

        #sin(angle) used here to complete equation variables
        if self.vertical_force_y == "" and self.vertical_force != "":
            self.ids.vertical_force_y.text = str(f"{self.vertical_force * self.vertical_force_sin_angle:,.6f}")
        elif self.vertical_force_y != "" and self.vertical_force == "":
            self.ids.vertical_force.text = str(f"{self.vertical_force_y / self.vertical_force_sin_angle:,.6f}")

    def reset(self):
        self.ids.vertical_force_y.text = ""
        self.ids.vertical_force.text = ""
        self.ids.vertical_force_angle.text = ""
        self.ids.vertical_force_sin_angle.text = ""
    
class HorzForce(Screen):
    def __init__(self, **kwargs):
        super(HorzForce, self).__init__(**kwargs)

    def calculate(self):
        """Pulls text input from kivy form for VertForce screen.  Checks for minimum inputs and calculates Newtons and Degrees"""
        self.horz_force_x = convert_float(self.ids.horz_force_x.text)
        self.horz_force = convert_float(self.ids.horz_force.text)
        self.horz_force_angle = convert_float(self.ids.horz_force_angle.text)
        self.horz_force_cos_angle = convert_float(self.ids.horz_force_cos_angle.text)
        
        #One way or another the cos(angle) will be produced for use later
        if self.horz_force_cos_angle == "" and self.horz_force_angle != "":
            self.horz_force_cos_angle = cos(radians(self.horz_force_angle))
            self.ids.horz_force_cos_angle.text = str(f"{self.horz_force_cos_angle:,.6f}")

        elif self.horz_force_cos_angle != "" and self.horz_force_angle == "":
            self.ids.horz_force_angle.text = str(f"{degrees(acos(self.horz_force_cos_angle)):,.6f}")

        elif self.horz_force_cos_angle != "" and self.horz_force_angle != "":
            if str(f'{degrees(acos(self.horz_force_cos_angle)):,.2f}') != str(f'{self.horz_force_angle:,.2f}'):
                error_popup = Popup(title='Check values!', content=Label(text='cos(angle) and angle don\'t match'), size_hint=(0.7, 0.7))
                error_popup.open()
            #self.ids.horz_force_cos_angle.text = str(f"{self.horz_force_cos_angle:,.6f}")
            #self.ids.horz_force_angle.text = str(f"{self.horz_force_angle:,.6f}")

        elif self.horz_force_x != "" and self.horz_force != "":
            self.horz_force_cos_angle = self.horz_force_x / self.horz_force
            self.ids.horz_force_cos_angle.text = str(f"{self.horz_force_cos_angle:,.6f}")
            self.ids.horz_force_angle.text = str(f"{degrees(acos(self.horz_force_cos_angle)):,.6f}")

        else:
            error_popup = Popup(title='Need more info!', content=Label(text='Not enough values to complete'), size_hint=(0.7, 0.7))
            error_popup.open()
        
        #cos(angle) used here to complete equation variables
        if self.horz_force_x == "" and self.horz_force != "":
            self.ids.horz_force_x.text = str(f"{self.horz_force * self.horz_force_cos_angle:,.6f}")
        elif self.horz_force_x != "" and self.horz_force == "":
            self.ids.horz_force.text = str(f"{self.horz_force_x/ self.horz_force_cos_angle:,.6f}")

    def reset(self):
        self.ids.horz_force_x.text = ""
        self.ids.horz_force.text = ""
        self.ids.horz_force_angle.text = ""
        self.ids.horz_force_cos_angle.text = ""

class Fsqrt(Screen):
    def __init__(self, **kwargs):
        super(Fsqrt, self).__init__(**kwargs)
     
    def calculate(self):
        self.Force = convert_float(self.ids.Force.text)
        self.Fx = convert_float(self.ids.Fx.text)
        self.Fy = convert_float(self.ids.Fy.text)

        if self.Force == "" and self.Fx != "" and self.Fy != "":
            self.ids.Force.text = str(f'{sqrt(self.Fx**2 + self.Fy**2):,.6f}')
        elif self.Force != "" and self.Fx == "" and self.Fy != "":
            self.ids.Fx.text = str(f'{sqrt(self.Force**2 - self.Fy**2):,.6f}')
        elif self.Force != "" and self.Fx != "" and self.Fy == "":
            self.ids.Fy.text = str(f'{sqrt(self.Force**2 - self.Fx**2):,.6f}')
        else:
            error_popup = Popup(title='Need more info!', content=Label(text='Not enough values to complete'), size_hint=(0.7, 0.7))
            error_popup.open()

    def reset(self):
        self.ids.Force.text = ""
        self.ids.Fx.text = ""
        self.ids.Fy.text = ""

class Theta(Screen):
    def __init__(self, **kwargs):
        super(Theta, self).__init__(**kwargs)
    
    def calculate(self):
        self.angle = convert_float(self.ids.angle.text)
        self.sin_angle = convert_float(self.ids.sin_angle.text)
        self.cos_angle = convert_float(self.ids.cos_angle.text)

        if type(self.angle) == str and type(self.sin_angle) != str and type(self.cos_angle) != str:
            self.ids.angle.text = str(f'{degrees(atan(self.sin_angle/self.cos_angle)):,.4f}')
        elif type(self.angle) == str and type(self.sin_angle) != str and type(self.cos_angle) == str:
            self.ids.angle.text = str(f'{degrees(asin(self.sin_angle)):,.4f}')
            self.ids.cos_angle.text = str(f'{cos((asin(self.sin_angle))):,.4f}')
        elif type(self.angle) == str and type(self.sin_angle) == str and type(self.cos_angle) != str:
            self.ids.angle.text = str(f'{degrees(acos(self.cos_angle)):,.4f}')
            self.ids.sin_angle.text = str(f'{sin((acos(self.cos_angle))):,.4f}')
        elif type(self.angle) != str and type(self.sin_angle) == str and type(self.cos_angle) == str:
            self.ids.cos_angle.text = str(f'{cos(radians(self.angle)):,.4f}')
            self.ids.sin_angle.text = str(f'{sin(radians(self.angle)):,.4f}')
        else:
            error_popup = Popup(title='Need more info!', content=Label(text='Not enough values to complete'), size_hint=(0.7, 0.7))
            error_popup.open()


    def reset(self):
        self.ids.angle.text = ""
        self.ids.sin_angle.text = ""
        self.ids.cos_angle.text = ""

class Polar(Screen):
    def __init__(self, **kwargs):
        super(Polar, self).__init__(**kwargs)

    def calculate(self):
        self.vector_value = self.ids.vector_value.text
        self.i_value = self.ids.i_value.text
        self.j_value = self.ids.j_value.text

        if self.vector_value != "":
            try:
                self.vector_list = self.vector_value.split("@")
                self.vector_mag, self.vector_degree = self.vector_list
                self.vector_mag, self.vector_degree = float(self.vector_mag.strip()), float(self.vector_degree.strip())
            except ValueError:
                print(ValueError)
            if type(self.vector_mag) == float and type(self.vector_degree) == float:
                self.ids.i_value.text = str(f'{self.vector_mag*cos(radians(self.vector_degree)):,.5f} i')
                self.ids.j_value.text = str(f'{self.vector_mag*sin(radians(self.vector_degree)):,.5f} j')

        if self.vector_value == "" and self.i_value != "" and self.j_value != "":
            if self.i_value.isdigit() and self.j_value.isdigit():
                try:
                    self.i_value = float(self.i_value)
                    self.j_value = float(self.j_value)
                except ValueError:
                    print(ValueError)
            else:
                for i in range(len(self.i_value[::-1])):
                    if self.i_value[i].isalpha():
                        self.i_value = self.i_value[:i]
                for j in range(len(self.j_value[::-1])):
                    if self.j_value[j].isalpha():
                        self.j_value = self.j_value[:j]
                try:
                    self.i_value = float(self.i_value)
                    self.j_value = float(self.j_value)
                except ValueError:
                    print(ValueError)
                self.ids.i_value.text = str(f'{self.i_value}')
                self.ids.j_value.text = str(f'{self.j_value}')
            if type(self.i_value) == float and type(self.j_value) == float:
                self.ids.vector_value.text = str(f'{sqrt(self.i_value**2 + self.j_value**2):,.5f} @ {degrees(atan(self.j_value/self.i_value)):,.5f}')

    def reset(self):
        self.ids.vector_value.text = ""
        self.ids.i_value.text = ""
        self.ids.j_value.text = ""

class Density(Screen):
    def __init__(self, **kwargs):
        super(Density, self).__init__(**kwargs)

    def calculate(self):
        self.density = convert_float(self.ids.density.text)
        self.mass = convert_float(self.ids.mass.text)
        self.volume = convert_float(self.ids.volume.text)

        if self.density == "" and self.mass != "" and self.volume != "":
            self.ids.density.text = str(f'{self.mass/self.volume:,.6f}')
        elif self.density != "" and self.mass != "" and self.volume == "":
            self.ids.volume.text = str(f'{self.mass/self.density:,.6f}')
        elif self.density != "" and self.mass == "" and self.volume != "":
            self.ids.mass.text = str(f'{self.density*self.volume:,.6f}')
        else:
            error_popup = Popup(title='Need more info!', content=Label(text='Not enough values to complete'), size_hint=(0.7, 0.7))
            error_popup.open()

    def reset(self):
        self.ids.density.text = ""
        self.ids.mass.text = ""
        self.ids.volume.text = ""

class Temps(Screen):
    def __init__(self, **kwargs):
        super(Temps, self).__init__(**kwargs)

    def calculate(self):
        self.temp_f = convert_float(self.ids.temp_f.text)
        self.temp_c = convert_float(self.ids.temp_c.text)
        self.temp_k = convert_float(self.ids.temp_k.text)
        if self.temp_f != "":
            self.temp_c = 5/9*((self.temp_f)- 32)
            self.temp_k = self.temp_c + 273
            self.ids.temp_c.text = str(f'{self.temp_c:,.4f}C')
            self.ids.temp_k.text = str(f'{self.temp_k:,.4f}K')
        if self.temp_c != "":
            self.temp_f = ((9/5)*self.temp_c) + 32
            self.temp_k = self.temp_c + 273
            self.ids.temp_f.text = str(f'{self.temp_f:,.4f}F')
            self.ids.temp_k.text = str(f'{self.temp_k:,.4f}K')
        if self.temp_k != "":
            self.temp_c = self.temp_k - 273
            self.temp_f = ((9/5)*self.temp_c) + 32
            self.ids.temp_c.text = str(f'{self.temp_c:,.4f}C')
            self.ids.temp_f.text = str(f'{self.temp_f:,.4f}F')
            self.ids.temp_k.text = str(f'{self.temp_k:,.4f}K')

    def reset(self):
        self.ids.temp_f.text = ""
        self.ids.temp_c.text = ""
        self.ids.temp_k.text = ""

class Ave_Vel(Screen):
    def __init__(self, **kwargs):
        super(Ave_Vel, self).__init__(**kwargs)

    def calculate(self):
        self.ave_vel = convert_float(self.ids.ave_vel.text)
        self.dist_x2 = convert_float(self.ids.dist_x2.text)
        self.dist_x1 = convert_float(self.ids.dist_x1.text)
        self.time2 = convert_float(self.ids.time2.text)
        self.time1 = convert_float(self.ids.time1.text)

        if self.ave_vel == "" and self.dist_x2 != "" and self.dist_x1 != "" and self.time2 != "" and self.time1 != "":
            self.ids.ave_vel.text = str(f'{(self.dist_x2 - self.dist_x1) / (self.time2 - self.time1):,.5f}')

        elif self.ave_vel != "" and self.dist_x2 == "" and self.dist_x1 != "" and self.time2 != "" and self.time1 != "":
            self.ids.dist_x2.text = str(f'{self.ave_vel*(self.time2 - self.time1) + self.dist_x1:,.5f}')

        elif self.ave_vel != "" and self.dist_x2 != "" and self.dist_x1 == "" and self.time2 != "" and self.time1 != "":
            self.ids.dist_x1.text = str(f'{self.dist_x2 - self.ave_vel*(self.time2 - self.time1):,.5f}')

        elif self.ave_vel != "" and self.dist_x2 != "" and self.dist_x1 != "" and self.time2 == "" and self.time1 != "":
            self.ids.time2.text = str(f'{(((self.dist_x2 - self.dist_x1)/self.ave_vel) + self.time1):,.5f}')

        elif self.ave_vel != "" and self.dist_x2 != "" and self.dist_x1 != "" and self.time2 != "" and self.time1 == "":
            self.ids.time1.text = str(f'{(self.time2 - ((self.dist_x2 - self.dist_x1)/self.ave_vel)):,.5f}')
        else:
            error_popup = Popup(title='Need more info!', content=Label(text='Not enough values to complete'), size_hint=(0.7, 0.7))
            error_popup.open()

    def reset(self):
        self.ids.ave_vel.text = ""
        self.ids.dist_x2.text = ""
        self.ids.dist_x1.text = ""
        self.ids.time2.text = ""
        self.ids.time1.text = ""

class Ave_Acc(Screen):
    def __init__(self, **kwargs):
        super(Ave_Acc, self).__init__(**kwargs)

    def calculate(self):
        self.ave_acc = convert_float(self.ids.ave_acc.text)
        self.vel2 = convert_float(self.ids.vel2.text)
        self.vel1 = convert_float(self.ids.vel1.text)
        self.time2 = convert_float(self.ids.time2.text)
        self.time1 = convert_float(self.ids.time1.text)

        if self.ave_acc == "" and self.vel2 != "" and self.vel1 != "" and self.time2 != "" and self.time1 != "":
            self.ids.ave_acc.text = str(f'{(self.vel2 - self.vel1) / (self.time2 - self.time1):,.5f}')

        elif self.ave_acc != "" and self.vel2 == "" and self.vel1 != "" and self.time2 != "" and self.time1 != "":
            self.ids.vel2.text = str(f'{self.ave_acc*(self.time2 - self.time1) + self.vel1:,.5f}')

        elif self.ave_acc != "" and self.vel2 != "" and self.vel1 == "" and self.time2 != "" and self.time1 != "":
            self.ids.vel1.text = str(f'{self.vel2 - self.ave_acc*(self.time2 - self.time1):,.5f}')

        elif self.ave_acc != "" and self.vel2 != "" and self.vel1 != "" and self.time2 == "" and self.time1 != "":
            self.ids.time2.text = str(f'{(((self.vel2 - self.vel1)/self.ave_acc) + self.time1):,.5f}')

        elif self.ave_acc != "" and self.vel2 != "" and self.vel1 != "" and self.time2 != "" and self.time1 == "":
            self.ids.time1.text = str(f'{(self.time2 - ((self.vel2 - self.vel1)/self.ave_acc)):,.5f}')
        else:
            error_popup = Popup(title='Need more info!', content=Label(text='Not enough values to complete'), size_hint=(0.7, 0.7))
            error_popup.open()
            

    def reset(self):
        self.ids.ave_acc.text = ""
        self.ids.vel2.text = ""
        self.ids.vel1.text = ""
        self.ids.time2.text = ""
        self.ids.time1.text = ""


class MyScreenManager(ScreenManager):
    pass

class MenuButtons(BoxLayout):
    def __init__(self, **kwargs):
        super(MenuButtons, self).__init__(**kwargs)
        """
        self.Friction_static = Button(text="Fs = us(Fn)", color=(1, 0.5, 0.5), bold=True)
        self.sum_moments = Button(text="Sigma(M) = (clockwise F*D) - (counterclockwise F*D)", color=(1, 0, 0), bold=True)
        self.torque = Button(text="Torque = F*D = FLsin(theta)", color=(0, 1, 0), bold=True)
        self.force = Button(text="F = ma", color=(0, 0.3, 1), bold=True)
        self.weight = Button(text="w = mg", color=(1, 0.5, 0.5), bold=True)
        self.work = Button(text="work = F * D", color=(1, 0, 0), bold=True)
        self.mech_adv = Button(text="MA = Force Out / Force In", color=(0, 1, 0), bold=True)
        self.force_accel_x = Button(text="Fcos(theta) = ma", color=(0, 0.3, 1), bold=True)
        self.force_accel_y = Button(text="Fsin(theta) = ma", color=(1, 0.5, 0.5), bold=True)
        self.displacement = Button(text="Change X = Vot + 1/2 at^2", color=(1, 0, 0), bold=True)
        self.motion = Button(text="v(t) = Vo + at", color=(0, 1, 0), bold=True)
        self.spec_heat = Button(text="Q = mc deltaT", color=(0, 0.3, 1), bold=True)
        self.impulse_momentum = Button(text="F deltaT = delta mv", color=(1, 0.5, 0.5), bold=True)
        
        self.add_widget(self.vert_force)
        self.add_widget(self.horz_force)
        self.add_widget(self.vect_force)
        self.add_widget(self.theta)
        self.add_widget(self.polar)
        self.add_widget(self.density)
        self.add_widget(self.celsius)
        self.add_widget(self.faren)
        self.add_widget(self.kelvin)
        self.add_widget(self.ave_vel)
        self.add_widget(self.ave_acc)
        self.add_widget(self.Friction_static)
        self.add_widget(self.sum_moments)
        self.add_widget(self.torque)
        self.add_widget(self.force)
        self.add_widget(self.weight)
        self.add_widget(self.work)
        self.add_widget(self.mech_adv)
        self.add_widget(self.force_accel_x)
        self.add_widget(self.force_accel_y)
        self.add_widget(self.displacement)
        self.add_widget(self.motion)
        self.add_widget(self.spec_heat)
        self.add_widget(self.impulse_momentum)
"""        

kv_file = Builder.load_file("physics.kv")

class PhysicsApp(App):
    def build(self):
        return kv_file

if __name__ == "__main__":
    PhysicsApp().run()
