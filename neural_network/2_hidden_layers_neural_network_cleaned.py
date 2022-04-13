

import numpy


class TwoHiddenLayerNeuralNetwork:
    def __init__(self, input_array: numpy.ndarray, output_array: numpy.ndarray) -> None:
        

        
        self.input_array = input_array

        
        
        

        
        
        
        self.input_layer_and_first_hidden_layer_weights = numpy.random.rand(
            self.input_array.shape[1], 4
        )

        
        
        
        self.first_hidden_layer_and_second_hidden_layer_weights = numpy.random.rand(
            4, 3
        )

        
        
        
        self.second_hidden_layer_and_output_layer_weights = numpy.random.rand(3, 1)

        
        self.output_array = output_array

        
        
        self.predicted_output = numpy.zeros(output_array.shape)

    def feedforward(self) -> numpy.ndarray:
        
        
        
        self.layer_between_input_and_first_hidden_layer = sigmoid(
            numpy.dot(self.input_array, self.input_layer_and_first_hidden_layer_weights)
        )

        
        
        self.layer_between_first_hidden_layer_and_second_hidden_layer = sigmoid(
            numpy.dot(
                self.layer_between_input_and_first_hidden_layer,
                self.first_hidden_layer_and_second_hidden_layer_weights,
            )
        )

        
        
        self.layer_between_second_hidden_layer_and_output = sigmoid(
            numpy.dot(
                self.layer_between_first_hidden_layer_and_second_hidden_layer,
                self.second_hidden_layer_and_output_layer_weights,
            )
        )

        return self.layer_between_second_hidden_layer_and_output

    def back_propagation(self) -> None:
        

        updated_second_hidden_layer_and_output_layer_weights = numpy.dot(
            self.layer_between_first_hidden_layer_and_second_hidden_layer.T,
            2
            * (self.output_array - self.predicted_output)
            * sigmoid_derivative(self.predicted_output),
        )
        updated_first_hidden_layer_and_second_hidden_layer_weights = numpy.dot(
            self.layer_between_input_and_first_hidden_layer.T,
            numpy.dot(
                2
                * (self.output_array - self.predicted_output)
                * sigmoid_derivative(self.predicted_output),
                self.second_hidden_layer_and_output_layer_weights.T,
            )
            * sigmoid_derivative(
                self.layer_between_first_hidden_layer_and_second_hidden_layer
            ),
        )
        updated_input_layer_and_first_hidden_layer_weights = numpy.dot(
            self.input_array.T,
            numpy.dot(
                numpy.dot(
                    2
                    * (self.output_array - self.predicted_output)
                    * sigmoid_derivative(self.predicted_output),
                    self.second_hidden_layer_and_output_layer_weights.T,
                )
                * sigmoid_derivative(
                    self.layer_between_first_hidden_layer_and_second_hidden_layer
                ),
                self.first_hidden_layer_and_second_hidden_layer_weights.T,
            )
            * sigmoid_derivative(self.layer_between_input_and_first_hidden_layer),
        )

        self.input_layer_and_first_hidden_layer_weights += (
            updated_input_layer_and_first_hidden_layer_weights
        )
        self.first_hidden_layer_and_second_hidden_layer_weights += (
            updated_first_hidden_layer_and_second_hidden_layer_weights
        )
        self.second_hidden_layer_and_output_layer_weights += (
            updated_second_hidden_layer_and_output_layer_weights
        )

    def train(self, output: numpy.ndarray, iterations: int, give_loss: bool) -> None:
        
        for iteration in range(1, iterations + 1):
            self.output = self.feedforward()
            self.back_propagation()
            if give_loss:
                loss = numpy.mean(numpy.square(output - self.feedforward()))
                print(f"Iteration {iteration} Loss: {loss}")

    def predict(self, input: numpy.ndarray) -> int:
        

        
        self.array = input

        self.layer_between_input_and_first_hidden_layer = sigmoid(
            numpy.dot(self.array, self.input_layer_and_first_hidden_layer_weights)
        )

        self.layer_between_first_hidden_layer_and_second_hidden_layer = sigmoid(
            numpy.dot(
                self.layer_between_input_and_first_hidden_layer,
                self.first_hidden_layer_and_second_hidden_layer_weights,
            )
        )

        self.layer_between_second_hidden_layer_and_output = sigmoid(
            numpy.dot(
                self.layer_between_first_hidden_layer_and_second_hidden_layer,
                self.second_hidden_layer_and_output_layer_weights,
            )
        )

        return int(self.layer_between_second_hidden_layer_and_output > 0.6)


def sigmoid(value: numpy.ndarray) -> numpy.ndarray:
    
    return 1 / (1 + numpy.exp(-value))


def sigmoid_derivative(value: numpy.ndarray) -> numpy.ndarray:
    
    return (value) * (1 - (value))


def example() -> int:
    
    
    input = numpy.array(
        (
            [0, 0, 0],
            [0, 0, 1],
            [0, 1, 0],
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 1],
        ),
        dtype=numpy.float64,
    )

    
    output = numpy.array(([0], [1], [1], [0], [1], [0], [0], [1]), dtype=numpy.float64)

    
    neural_network = TwoHiddenLayerNeuralNetwork(input_array=input, output_array=output)

    
    
    neural_network.train(output=output, iterations=10, give_loss=False)

    return neural_network.predict(numpy.array(([1, 1, 1]), dtype=numpy.float64))


if __name__ == "__main__":
    example()
