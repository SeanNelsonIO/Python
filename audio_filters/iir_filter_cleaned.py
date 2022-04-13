from __future__ import annotations


class IIRFilter:
    

    def __init__(self, order: int) -> None:
        self.order = order

        
        self.a_coeffs = [1.0] + [0.0] * order
        
        self.b_coeffs = [1.0] + [0.0] * order

        
        self.input_history = [0.0] * self.order
        
        self.output_history = [0.0] * self.order

    def set_coefficients(self, a_coeffs: list[float], b_coeffs: list[float]) -> None:
        
        if len(a_coeffs) < self.order:
            a_coeffs = [1.0] + a_coeffs

        if len(a_coeffs) != self.order + 1:
            raise ValueError(
                f"Expected a_coeffs to have {self.order + 1} elements for {self.order}"
                f"-order filter, got {len(a_coeffs)}"
            )

        if len(b_coeffs) != self.order + 1:
            raise ValueError(
                f"Expected b_coeffs to have {self.order + 1} elements for {self.order}"
                f"-order filter, got {len(a_coeffs)}"
            )

        self.a_coeffs = a_coeffs
        self.b_coeffs = b_coeffs

    def process(self, sample: float) -> float:
        
        result = 0.0

        
        for i in range(1, self.order + 1):
            result += (
                self.b_coeffs[i] * self.input_history[i - 1]
                - self.a_coeffs[i] * self.output_history[i - 1]
            )

        result = (result + self.b_coeffs[0] * sample) / self.a_coeffs[0]

        self.input_history[1:] = self.input_history[:-1]
        self.output_history[1:] = self.output_history[:-1]

        self.input_history[0] = sample
        self.output_history[0] = result

        return result
