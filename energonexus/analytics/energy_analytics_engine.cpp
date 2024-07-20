#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

class EnergyAnalyticsEngine {
public:
    EnergyAnalyticsEngine(std::vector<std::pair<double, double>> energyData) : energyData_(energyData) {}

    double calculateMeanEnergyConsumption() {
        double sum = 0.0;
        for (const auto& data : energyData_) {
            sum += data.first;
        }
        return sum / energyData_.size();
    }

    double calculateStandardDeviationEnergyConsumption() {
        double mean = calculateMeanEnergyConsumption();
        double sum = 0.0;
        for (const auto& data : energyData_) {
            sum += pow(data.first - mean, 2);
        }
        return sqrt(sum / energyData_.size());
    }

    std::vector<std::pair<double, double>> getEnergyData() {
        return energyData_;
    }

private:
    std::vector<std::pair<double, double>> energyData_;
};

int main() {
    std::vector<std::pair<double, double>> energyData = {{10.0, 20.0}, {15.0, 30.0}, {20.0, 40.0}};
    EnergyAnalyticsEngine engine(energyData);

    std::cout << "Mean energy consumption: " << engine.calculateMeanEnergyConsumption() << std::endl;
    std::cout << "Standard deviation of energy consumption: " << engine.calculateStandardDeviationEnergyConsumption() << std::endl;

    return 0;
}
