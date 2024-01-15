import matplotlib.pyplot as plt
import pandas as pd


T_OMGEVING = 20
T0_KOFFIE = 90  # begintemperatuur van de koffie
d_koffie = T0_KOFFIE - T_OMGEVING
AFKOELINGSCOEFFICIENT = 0.82

# begintijd in minuten
T0 = 0


def T(t):
    """t is de delta tijd in minuten"""
    afkoelings_coeff = AFKOELINGSCOEFFICIENT**t

    return T_OMGEVING + d_koffie * afkoelings_coeff


def delta_T(t0, t1):
    return (T(t1) - T(t0)) / (t1 - t0)


def plot_tabel(x_reeks, y_reeks, titel, x_label, y_label):
    plt.figure(figsize=(10, 6))
    plt.plot(x_reeks, y_reeks, marker="o")  # 'o' marks each point on the plot
    plt.title(titel)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()


def main():
    tijd = list(range(0, 65, 5))
    temp_daling = [T(t) for t in tijd]

    t_diff = []
    d_temp = []

    for i, d_tijd in enumerate(
        tijd
    ):  # enumerate geeft index en waarde voor elke waarde in de lijst
        if i == 0:  # begin, nog geen tijd gehad om af te koelen
            t_diff.append(0)
            d_temp.append(T0_KOFFIE)
        else:
            d_coeff = delta_T(tijd[i - 1], d_tijd)
            t_diff.append(d_coeff)
            d_temp.append(d_temp[i - 1] + (d_tijd - tijd[i - 1]) * d_coeff)

    row_names = ["coeff", "temp"]
    df = pd.DataFrame([t_diff, d_temp], index=row_names, columns=tijd)

    # print tabel
    print(df)

    # print diff coeff
    plot_tabel(
        x_reeks=tijd,
        y_reeks=t_diff,
        titel="koffie afkoeling: diff coeff",
        x_label="tijd (min)",
        y_label="°C/min",
    )

    # print temp
    plot_tabel(
        x_reeks=tijd,
        y_reeks=d_temp,
        titel="koffie afkoeling: temperatuur",
        x_label="tijd (min)",
        y_label="°C",
    )


if __name__ == "__main__":
    main()
