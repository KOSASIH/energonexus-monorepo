import matplotlib.pyplot as plt

def visualize_energy_production(production_data):
    # visualize energy production data using Matplotlib
    plt.plot(production_data)
    plt.xlabel('Time')
    plt.ylabel('Energy Production')
    plt.title('Energy Production Over Time')
    plt.show()

def visualize_energy_consumption(consumption_data):
    # visualize energy consumption data using Matplotlib
    plt.plot(consumption_data)
    plt.xlabel('Time')
    plt.ylabel('Energy Consumption')
    plt.title('Energy Consumption Over Time')
    plt.show()

def visualize_energy_storage(storage_data):
    # visualize energy storage data using Matplotlib
    plt.plot(storage_data)
    plt.xlabel('Time')
    plt.ylabel('Energy Storage')
    plt.title('Energy Storage Over Time')
    plt.show()
