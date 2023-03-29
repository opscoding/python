def is_criticality_balanced(temperature, neutrons_emitted):
    """
    A reactor is said to be critical if it satisfies the following conditions:

    The temperature is less than 800 K.
    The number of neutrons emitted per second is greater than 500.
    The product of temperature and neutrons emitted per second is less than 500000.
    Implement the function is_criticality_balanced() that takes temperature measured in kelvin and neutrons_emitted as parameters, and returns True if the criticality conditions are met, False if not.
    """
    return (temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted < 500000))

def reactor_efficiency(voltage, current, theoretical_max_power):
    """
    Once the reactor has started producing power its efficiency needs to be determined. Efficiency can be grouped into 4 bands:

    green -> efficiency of 80% or more,
    orange -> efficiency of less than 80% but at least 60%,
    red -> efficiency below 60%, but still 30% or more,
    black -> less than 30% efficient.

    The percentage value can be calculated as (generated_power/theoretical_max_power)*100 where generated_power = voltage * current.
    """
    generated_power = ((voltage * current) / theoretical_max_power)*100
    if int(generated_power) >= 80:
        return 'green'
    elif int(generated_power) < 80 and int(generated_power) >= 60:
        return 'orange'
    elif int(generated_power) >= 30 and int(generated_power) < 60:
        return 'red'
    return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """
    If temperature * neutrons_produced_per_second < 90% of threshold, output a status code of 'LOW' indicating that control rods must be removed to produce power.

    If temperature * neutrons_produced_per_second are within plus or minus 10% of the threshold the reactor is in criticality and the status code of 'NORMAL' should be output, indicating that the reactor is in optimum condition and control rods are in an ideal position.

    If temperature * neutrons_produced_per_second is not in the above-stated ranges, the reactor is going into meltdown and a status code of 'DANGER' must be passed to immediately shut down the reactor.
    """
    if (temperature * neutrons_produced_per_second) < (threshold * 0.9):
        return 'LOW'
    elif int((temperature * neutrons_produced_per_second) / (threshold) * 100) < 110:
        return 'NORMAL'
    return 'DANGER'


if __name__ == '__main__':
    print(is_criticality_balanced(750, 600))
    print(reactor_efficiency(200, 50, 15000))
    print(fail_safe(temperature=10, neutrons_produced_per_second=1101, threshold=10000))