# EPlus_BiquadraticCurveCoeffs
Calculation of coefficients from manufacturers' data for biquadratic curves associated to E+ objects related to heat pumps and chillers modelling.
z = C1 + C2x + C3x^2 + C4y + C5y^2 + C6xy

Heat Pump / Heating mode (Coil:WaterHeating:AirToWaterPump:Pumped)
Function(x=evaporator inlet air temperature, y=condenser inlet water temperature)
1. Heating Capacity Function of Temperature Curve 
2. Heating COP Function of Temperature Curve

Chiller (Chiller:Electric:EIR)
Function(x=leaving chilled water tempertature, y=entering fluid temp)
Cooling Capacity Function of Temperature Curve 
Electric Input to Cooling Output Ratio Function of Temperature Curve
