# Equations:
#1 V = V0 + a * (T - T0)
#2 X = X0 + V0 * T + 1/2 * A * T^2
#3 V^2 = V0^2 + 2 * a * (X - X0)

import tkinter as tk
from tkinter import *
import time
import math

def parse_text(text):
    text=text.strip()
    if text=="":
        return None
    try:
        return float(text)
    except ValueError:
        return None

def mainwindow():
    root=tk.Tk()
    root.title("Kinematics Calculator")
    root.geometry("700x300")

    root.configure(bg="gray")
# /////////////////////////////////////////////////---Data Entry Fields---////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                #       One-Dimensional UI
    root.X0_label=Label(root, text="1. Initial Position (X0):", bg="gray", fg="black", font=("helvetica", 12))
    root.X0_label.grid(row=10, column=10)
    root.X0_field=Entry(root, bg="white", fg="black", font=("helvetica", 12))
    root.X0_field.grid(row=10, column=11)

    root.V0_label=Label(root, text="2. Initial Velocity (V0):", bg="gray", fg="black", font=("helvetica", 12))
    root.V0_label.grid(row=11, column=10)
    root.V0_field=Entry(root, bg="white", fg="black", font=("helvetica", 12))
    root.V0_field.grid(row=11, column=11)

    root.a_label=Label(root, text="3. Acceleration (a):", bg="gray", fg="black", font=("helvetica", 12))
    root.a_label.grid(row=12, column=10)
    root.a_field=Entry(root, bg="white", fg="black", font=("helvetica", 12))
    root.a_field.grid(row=12, column=11)

    root.T0_label=Label(root, text="4. Initial Time (T0):", bg="gray", fg="black", font=("helvetica", 12))
    root.T0_label.grid(row=13, column=10)
    root.T0_field=Entry(root, bg="white", fg="black", font=("helvetica", 12))
    root.T0_field.grid(row=13, column=11)

    root.T_label=Label(root, text="5. Final Time (T):", bg="gray", fg="black", font=("helvetica", 12))
    root.T_label.grid(row=14, column=10)
    root.T_field=Entry(root, bg="white", fg="black", font=("helvetica", 12))
    root.T_field.grid(row=14, column=11)

    root.X_label=Label(root, text="6. Final Position (X):", bg="gray", fg="black", font=("helvetica", 12))
    root.X_label.grid(row=15, column=10)
    root.X_field=Entry(root, bg="white", fg="black", font=("helvetica", 12))
    root.X_field.grid(row=15, column=11)

    root.DX_label=Label(root, text="7. Displacement (^X):", bg="gray", fg="black", font=("helvetica", 12))
    root.DX_label.grid(row=16, column=10)
    root.DX_field=Entry(root, bg="white", fg="black", font=("helvetica", 12))
    root.DX_field.grid(row=16, column=11)

    root.V_label=Label(root, text="8. Final Velocity (V):", bg="gray", fg="black", font=("helvetica", 12))
    root.V_label.grid(row=17, column=10)
    root.V_field=Entry(root, bg="white", fg="black", font=("helvetica", 12))
    root.V_field.grid(row=17, column=11)

#///////////////////////////////////////////////////= Target Select =/////////////////////////////////////////////////////////////////////////
    root.Target_select_label=Label(root, text="Target Value no.: ", bg="silver", fg="red", font=("helvetica", 12))
    root.Target_select_label.grid(row=20, column=10)
    root.Target_select_field=Entry(root, bg="white", fg="black", font=("helvetica", 12))
    root.Target_select_field.grid(row=20, column=11)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                    Second UI Dimension

    root.Y0_label=Label(root, text="9. Initial Y Position (Y0): ", bg="gray", fg="black", font=("helvetica", 12))
    root.Y0_label.grid(row=10, column=14)
    root.Y0_field=Entry(root, bg="white", fg="black", font=("helvetica", 12))
    root.Y0_field.grid(row=10, column=15)

    root.Y_label=Label(root, text="10. Final Y Position (Y): ", bg="gray", fg="black", font=("helvetica", 12))
    root.Y_label.grid(row=11, column=14)
    root.Y_field=Entry(root, bg="white", fg="black", font=("helvetica", 12))
    root.Y_field.grid(row=11, column=15)

    root.Vy0_label=Label(root, text="11. Initial Y Velocity (Vy0): ", bg="gray", fg="black", font=("helvetica", 12))
    root.Vy0_label.grid(row=12, column=14)
    root.Vy0_field=Entry(root, bg="white", fg="black", font=("helvetica", 12))
    root.Vy0_field.grid(row=12, column=15)

    root.Vy_label=Label(root, text="12. Final Y Velocity (Vy): ", bg="gray", fg="black", font=("helvetica", 12))
    root.Vy_label.grid(row=13, column=14)
    root.Vy_field=Entry(root, bg="white", fg="black", font=("helvetica", 12))
    root.Vy_field.grid(row=13, column=15)

    root.Ay_label=Label(root, text="13. Y Acceleration (Ay): ", bg="gray", fg="black", font=("helvetica", 12))
    root.Ay_label.grid(row=14, column=14)
    root.Ay_field=Entry(root, bg="white", fg="black", font=("helvetica", 12))
    root.Ay_field.grid(row=14, column=15)

    root.DY_label=Label(root, text="14. Y Displacement (DY): ", bg="gray", fg="black", font=("helvetica", 12))
    root.DY_label.grid(row=15, column=14)
    root.DY_field=Entry(root, bg="white", fg="black", font=("helvetica", 12))
    root.DY_field.grid(row=15, column=15)

#//////////////////////////////////////////////////---Calculations---//////////////////////////////////////////////////////////////////////////
    def error_page(type):
        root.destroy()
        time.sleep(0.001)
        error_root=tk.Tk()
        error_root.title("Uh Oh...")
        error_root.geometry("800x600")
        error_root.configure(bg="red")

        if type=="error":
            chastisement=Label(error_root, text="You Broke Something. I am very dissappointed.", bg="red", fg="black", font=("helvetica", 22))
            chastisement.pack()
        else:
            chastisement=Label(error_root, text="Target Value cannot be calculated \n with the provided information.", bg="red", fg="black", font=("helvetica", 22))
            chastisement.pack()

        error_root.mainloop()


    def run_calculations():
        print("Calculating...")
        X0 = parse_text(root.X0_field.get())
        V0 = parse_text(root.V0_field.get())
        A = parse_text(root.a_field.get())
        T0 = parse_text(root.T0_field.get())
        T = parse_text(root.T_field.get())
        X = parse_text(root.X_field.get())
        DX = parse_text(root.DX_field.get())
        V = parse_text(root.V_field.get())

        Y0 = parse_text(root.Y0_field.get())
        Y = parse_text(root.Y_field.get())
        Vy0 = parse_text(root.Vy0_field.get())
        Vy = parse_text(root.Vy_field.get())
        Ay = parse_text(root.Ay_field.get())
        DY = parse_text(root.DY_field.get())

        Target_value = (root.Target_select_field.get())


        if Target_value == "1":
            print("Finding Initial Position...")
            if X is not None and V0 is not None and T is not None and T0 is not None and A is not None:
                friendly_little_friend= X - V0*(T - T0) - 0.5*A*(T - T0)**2
            elif X is not None and V is not None and V0 is not None and A is not None:
                friendly_little_friend= X - ((V**2 - V0**2) / (2*A))
            elif X is not None and DX is not None:
                friendly_little_friend= X - DX
            else:
                error_page("insufficient")

        elif Target_value == "2":
            print("Finding Initial Velocity...")
            if V is not None:
                friendly_little_friend= V0 + A(T-T0)
            elif X is not None and X0 is not None and T0 is not None and T is not None:
                friendly_little_friend= (X - X0 - 0.5*A* (T-T0)**2) / (T-T0)
            elif V is not None and A is not None and X is not None and X0 is not None:
                friendly_little_friend= math.sqrt(V**2 - 2*A*(X-X0))
            else:
                error_page("insufficient")

        elif Target_value == "3":
            print("Finding Acceleration...")
            if V is not None and V0 is not None and T is not None and T0 is not None:
                friendly_little_friend= (V - V0) / (T-T0)
            elif X is not None and X0 is not None and V0 is not None and T is not None and T0 is not None:
                friendly_little_friend= (2*(X - X0 - V0*(T - T0))) / (T - T0)**2
            elif V is not None and V0 is not None and X is not None and X0 is not None:
                friendly_little_friend= (V**2 - V0**2) / (2*(X - X0))
            else:
                error_page("insufficient")

        elif Target_value =="4":
            print("Finding Initial Time...")
            if V is not None and V0 is not None and A is not None:
                friendly_little_friend = T - (V - V0) / A
            elif X is not None and X0 is not None and V0 is not None and A is not None:
                a_coef = 0.5 * A
                b_coef = V0 - A * T
                c_coef = X0 - X
                discriminant = b_coef**2 - 4*a_coef*c_coef
                if discriminant < 0:
                    error_page("insufficient")
                else:
                    sqrt_disc = math.sqrt(discriminant)
                    delta_T0_1 = (-b_coef + sqrt_disc) / (2 * a_coef)
                    delta_T0_2 = (-b_coef - sqrt_disc) / (2 * a_coef)
                    delta_T0 = max(delta_T0_1, delta_T0_2)
                    friendly_little_friend = T - delta_T0
            else:
                error_page("insufficient")

        elif Target_value == "5":
            print("Finding Final Time...")
            if V is not None and V0 is not None and A is not None:
                friendly_little_friend = T0 + (V - V0) / A
            elif X is not None and X0 is not None and V0 is not None and A is not None:
                a_coef = 0.5 * A
                b_coef = V0
                c_coef = X0 - X
                discriminant = b_coef**2 - 4*a_coef*c_coef
                if discriminant < 0:
                    error_page("insufficient")
                else:
                    sqrt_disc = math.sqrt(discriminant)
                    delta_T1 = (-b_coef + sqrt_disc) / (2 * a_coef)
                    delta_T2 = (-b_coef - sqrt_disc) / (2 * a_coef)
                    delta_T = max(delta_T1, delta_T2)
                    friendly_little_friend = T0 + delta_T
            else:
                error_page("insufficient")

        elif Target_value == "6":
            print("Finding Final Position...")
            if X0 is not None and V0 is not None and T is not None and T0 is not None and A is not None:
                friendly_little_friend= X0 + V0*(T-T0) + 0.5*A*(T - T0)**2
            elif X is not None and V is not None and A is not None and V0 is not None:
                friendly_little_friend= X0 + ((V**2 - V0**2) / (2*A))
            elif X0 is not None and DX is not None:
                friendly_little_friend= X0 + DX
            else:
                error_page("insufficient")

        elif Target_value == "7":
            print("Finding Displacement...")
            if X is not None and X0 is not None:
                friendly_little_friend= X - X0
            elif V0 is not None and A is not None and T is not None and T0 is not None:
                friendly_little_friend= V0 * (T-T0) + 0.5*A*(T-T0)**2
            elif V is not None and V0 is not None and A is not None:
                friendly_little_friend= (V**2 - V0**2)/(2*A)
            else:
                error_page("insufficient")

        elif Target_value == "8":
            print("Finding Target Velocity...")
            if V0 is not None and T is not None and T0 is not None:
                friendly_little_friend= V0 + A * (T - T0)
            elif V0 is not None and A is not None and X0 is not None and X is not None:
                friendly_little_friend = (V0**2 + 2*A*(X - X0))**0.5
            else:
                error_page("insufficient")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////// Y Calculations
        elif Target_value == "9":
            print("Finding Initial Y Position...")
            if Y is not None and Vy0 is not None and T is not None and T0 is not None and Ay is not None:
                friendly_little_friend= Y - Vy0*(T - T0) - 0.5*Ay*(T - T0)**2
            elif Y is not None and Vy is not None and Vy0 is not None and Ay is not None:
                friendly_little_friend= Y - ((Vy**2 - Vy0**2) / (2*Ay))
            elif Y is not None and DY is not None:
                friendly_little_friend= Y - DY
            else:
                error_page("insufficient")

        elif Target_value == "10":
            print("Finding Initial Y Position...")
            if Y0 is not None and Vy0 is not None and T is not None and T0 is not None and Ay is not None:
                friendly_little_friend= Y0 + Vy0*(T-T0) + 0.5*Ay*(T - T0)**2
            elif Y is not None and Vy is not None and Ay is not None and Vy0 is not None:
                friendly_little_friend= Y0 + ((Vy**2 - Vy0**2) / (2*Ay))
            elif Y0 is not None and DY is not None:
                friendly_little_friend= Y0 + DY
            else:
                error_page("insufficient")

        elif Target_value == "11":
            print("Finding Initial Y Velocity...")
            if V is not None:
                friendly_little_friend= V + Ay(T-T0)
            elif Y is not None and Y0 is not None and T0 is not None and T is not None:
                friendly_little_friend= (Y - Y0 - 0.5*Ay* (T-T0)**2) / (T-T0)
            elif Vy is not None and Ay is not None and Y is not None and Y0 is not None:
                friendly_little_friend= math.sqrt(Vy**2 - 2*Ay*(Y-Y0))
            else:
                error_page("insufficient")

        elif Target_value == "12":
            print("Finding Final Y Velocity...")
            if Vy0 is not None and T is not None and T0 is not None:
                friendly_little_friend= Vy0 + Ay * (T - T0)
            elif Vy0 is not None and Ay is not None and Y0 is not None and Y is not None:
                friendly_little_friend = (Vy0**2 + 2*Ay*(Y - Y0))**0.5
            else:
                error_page("insufficient")

        elif Target_value == "13":
            print("Finding Y Acceleration...")
            if Vy is not None and Vy0 is not None and T is not None and T0 is not None:
                friendly_little_friend= (Vy - Vy0) / (T-T0)
            elif Y is not None and Y0 is not None and Vy0 is not None and T is not None and T0 is not None:
                friendly_little_friend= (2*(Y - Y0 - Vy0*(T - T0))) / (T - T0)**2
            elif Vy is not None and Vy0 is not None and Y is not None and Y0 is not None:
                friendly_little_friend= (Vy**2 - Vy0**2) / (2*(Y - Y0))
            else:
                error_page("insufficient")

        elif Target_value == "14":
            print("Finding Y Displacement...")
            if Y is not None and Y0 is not None:
                friendly_little_friend= Y - Y0
            elif Vy0 is not None and Ay is not None and T is not None and T0 is not None:
                friendly_little_friend= Vy0 * (T-T0) + 0.5*Ay*(T-T0)**2
            elif Vy is not None and Vy0 is not None and Ay is not None:
                friendly_little_friend= (Vy**2 - Vy0**2)/(2*Ay)
            else:
                error_page("insufficient")

        else:
            error_page("error")

        # print(X0,V0,A,T0,T,DX,V)

        print(friendly_little_friend)
        solution=tk.Label(root, font="Helvetica", bg="green", fg="silver", text= friendly_little_friend)
        solution.grid(row= 25, column= 10)


    root.Calc_button=Button(root, text="Calculate", bg="blue", fg="silver", font=("impact", 12), command=lambda:run_calculations())
    root.Calc_button.grid(row=22, column=15)

    root.mainloop()

mainwindow()