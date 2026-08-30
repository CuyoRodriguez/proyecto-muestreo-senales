import numbers

import numpy as np


def calcular_senal_continua(
	tiempo: np.ndarray,
	valor_inicial: float = 1.0,
	amplitud_pico: float = 3.0,
	tasa_subida: float = 1.2,
	tasa_disminucion: float = 0.18,
	frecuencia: float = 1.0,
) -> np.ndarray:
	"""Calcula una aproximacion suave de la señal continua e(t)."""
	# Es una aproximacion visual, porque el ejercicio original no proporciona
	# una ecuacion exacta para la señal.
	oscilacion = np.sin(2 * np.pi * frecuencia * tiempo)
	crecimiento = 1 - np.exp(-tasa_subida * tiempo)
	disminucion = np.exp(-tasa_disminucion * tiempo)

	return valor_inicial + amplitud_pico * oscilacion * crecimiento * disminucion


def calcular_instantes_muestreo(
	periodo_muestreo: float,
	tiempo_inicial: float,
	tiempo_final: float,
) -> np.ndarray:
	"""Devuelve los instantes t_k = kT contenidos en un intervalo temporal."""
	valores = (periodo_muestreo, tiempo_inicial, tiempo_final)
	if any(isinstance(valor, bool) or not isinstance(valor, numbers.Real) for valor in valores):
		raise TypeError("T, tiempo_inicial y tiempo_final deben ser números reales")

	periodo_muestreo = float(periodo_muestreo)
	tiempo_inicial = float(tiempo_inicial)
	tiempo_final = float(tiempo_final)

	if not np.isfinite(periodo_muestreo) or periodo_muestreo <= 0:
		raise ValueError("El período de muestreo T debe ser positivo y finito")
	if not np.isfinite(tiempo_inicial) or not np.isfinite(tiempo_final):
		raise ValueError("Los límites de tiempo deben ser finitos")
	if tiempo_inicial > tiempo_final:
		raise ValueError("El tiempo inicial no puede ser mayor que el tiempo final")

	indice_inicial = int(np.ceil(tiempo_inicial / periodo_muestreo))
	indice_final = int(np.floor(tiempo_final / periodo_muestreo))
	if indice_inicial > indice_final:
		return np.array([], dtype=float)

	indices = np.arange(indice_inicial, indice_final + 1)
	return indices * periodo_muestreo


def calcular_valores_muestreados(
	periodo_muestreo: float,
	tiempo_inicial: float,
	tiempo_final: float,
) -> tuple[np.ndarray, np.ndarray]:
	"""Devuelve los instantes de muestreo y los valores correspondientes e(kT)."""
	instantes = calcular_instantes_muestreo(
		periodo_muestreo,
		tiempo_inicial,
		tiempo_final,
	)
	valores = calcular_senal_continua(instantes)

	return instantes, valores
