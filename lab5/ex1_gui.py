import tkinter as tk

# calcularea valorilor reale ale datelor
x_real = 5/7
y_real = 1/3
suma_real = x_real + y_real
produs_real = x_real * y_real
dif_real = x_real - y_real
cat_real = x_real / y_real

# setarea valorilor aproximative
x_aprox = 0.71428 * 10 ** 0
y_aprox = 0.33333 * 10 ** 0

# calcularea valorilor aproximative
suma_aprox = x_aprox + y_aprox
produs_aprox = x_aprox * y_aprox
dif_aprox = x_aprox - y_aprox
cat_aprox = x_aprox / y_aprox

# calcularea erorilor absolute si relative
suma_err_abs = abs(suma_real - suma_aprox)
suma_err_rel = suma_err_abs / suma_real
produs_err_abs = abs(produs_real - produs_aprox)
produs_err_rel = produs_err_abs / produs_real
dif_err_abs = abs(dif_real - dif_aprox)
dif_err_rel = dif_err_abs / dif_real
cat_err_abs = abs(cat_real - cat_aprox)
cat_err_rel = cat_err_abs / cat_real

# functia pentru afisarea valorilor
def show_values():
    # rotunjirea valorilor aproximative la 5 zecimale
    x_aprox_rounded = round(x_aprox, 5)
    y_aprox_rounded = round(y_aprox, 5)
    suma_aprox_rounded = round(suma_aprox, 5)
    produs_aprox_rounded = round(produs_aprox, 5)
    dif_aprox_rounded = round(dif_aprox, 5)
    cat_aprox_rounded = round(cat_aprox, 5)

    # rotunjirea erorilor absolute si relative la 6 zecimale
    suma_err_abs_rounded = round(suma_err_abs, 6)
    suma_err_rel_rounded = round(suma_err_rel, 6)
    produs_err_abs_rounded = round(produs_err_abs, 6)
    produs_err_rel_rounded = round(produs_err_rel, 6)
    dif_err_abs_rounded = round(dif_err_abs, 6)
    dif_err_rel_rounded = round(dif_err_rel, 6)
    cat_err_abs_rounded = round(cat_err_abs, 6)
    cat_err_rel_rounded = round(cat_err_rel, 6)
    
    # afisarea valorilor aproximative 
    x_aprox_label.config(text=f"x_aprox: {x_aprox_rounded}")
    y_aprox_label.config(text=f"y_aprox: {y_aprox_rounded}")
    suma_aprox_label.config(text=f"suma_aprox: {suma_aprox_rounded}")
    produs_aprox_label.config(text=f"produs_aprox: {produs_aprox_rounded}")
    dif_aprox_label.config(text=f"diferenta_aprox: {dif_aprox_rounded}")
    cat_aprox_label.config(text=f"cat_aprox: {cat_aprox_rounded}")
    
    # afisarea erorilor absolute si relative
    suma_err_abs_label.config(text=f"suma_err_abs: {suma_err_abs_rounded}")
    suma_err_rel_label.config(text=f"suma_err_rel: {suma_err_rel_rounded}")
    produs_err_abs_label.config(text=f"produs_err_abs: {produs_err_abs_rounded}")
    produs_err_rel_label.config(text=f"produs_err_rel: {produs_err_rel_rounded}")
    dif_err_abs_label.config(text=f"diferenta_err_abs: {dif_err_abs_rounded}")
    dif_err_rel_label.config(text=f"diferenta_err_rel: {dif_err_rel_rounded}")
    cat_err_abs_label.config(text=f"cat_err_abs: {cat_err_abs_rounded}")
    cat_err_rel_label.config(text=f"cat_err_rel:{cat_err_rel_rounded}")
    
  
#crearea interfetei grafice    
root = tk.Tk()
root.geometry("400x400")
root.title("Calcul Numeric")

#crearea etichetelor pentru valorile de intrare
x_real_label = tk.Label(root, text=f"x_real: {x_real}")
x_real_label.pack()
y_real_label = tk.Label(root, text=f"y_real: {y_real}")
y_real_label.pack()

#crearea etichetelor pentru valorile aproximative
x_aprox_label = tk.Label(root)
x_aprox_label.pack()
y_aprox_label = tk.Label(root)
y_aprox_label.pack()
suma_aprox_label = tk.Label(root)
suma_aprox_label.pack()
produs_aprox_label = tk.Label(root)
produs_aprox_label.pack()
dif_aprox_label = tk.Label(root)
dif_aprox_label.pack()
cat_aprox_label = tk.Label(root)
cat_aprox_label.pack()

#crearea etichetelor pentru erorile absolute
suma_err_abs_label = tk.Label(root)
suma_err_abs_label.pack()
produs_err_abs_label = tk.Label(root)
produs_err_abs_label.pack()
dif_err_abs_label = tk.Label(root)
dif_err_abs_label.pack()
cat_err_abs_label = tk.Label(root)
cat_err_abs_label.pack()

#crearea etichetelor pentru erorile relative
suma_err_rel_label = tk.Label(root)
suma_err_rel_label.pack()
produs_err_rel_label = tk.Label(root)
produs_err_rel_label.pack()
dif_err_rel_label = tk.Label(root)
dif_err_abs_label.pack()
cat_err_rel_label = tk.Label(root)
cat_err_rel_label.pack()

#crearea butonului de afisare a valorilor
show_values_button = tk.Button(root, text="Afiseaza valorile", command=show_values)
show_values_button.pack()

root.mainloop()