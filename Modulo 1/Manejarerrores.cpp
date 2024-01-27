#include <iostream>
#include <stdexcept>
#include <sstream>

using namespace std;

int sumarNumeros(const string& input1, const string& input2) {
    try {
        // Convertir las cadenas de entrada a números enteros
        float numero1 = stoi(input1);
        float numero2 = stoi(input2);

        // Realizar la suma y devolver el resultado
        return numero1 + numero2;
    } catch (const std::exception& e) {
        // Manejar la excepción y mostrar un mensaje de error
        cerr << "Excepcion capturada, ingresaste texto en lugar de numeros " << endl;
        // Devolver un valor predeterminado en caso de error
        return 0;
    }
}

int main() {
    // Pedir al usuario que ingrese dos números
    string input1, input2;
    cout << "Ingrese el primer numero: ";
    cin >> input1;
    cout << "Ingrese el segundo numero: ";
    cin >> input2;

    // Realizar la suma y mostrar el resultado
    int resultado = sumarNumeros(input1, input2);
    cout << "Resultado de la suma: " << resultado << endl;

    return 0;
}

