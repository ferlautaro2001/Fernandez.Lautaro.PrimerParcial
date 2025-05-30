from normalizacion import normalizar_nombre_usuario, normalizar_empresas

usuarios_vip = [
    "lunatico_pixel", "sombra_cristal", "ecoerrante", "navefantasma",
    "bytesdelabahia", "tintaenelviento", "relojoxidado", "miradacodificada",
    "circuitoazul", "fuego_niebla", "teclaerrante", "nebulosa_urbana",
    "sueño_binario", "saltofantasma", "claveoculta"
]
empresas = ["Apple", "Tesla", "NVIDIA"]

precios = [10.41, 7.71, 8.50]

vip_normalizados = []
for i in range(len(usuarios_vip)):
    vip_normalizados += [normalizar_nombre_usuario(usuarios_vip[i])]

empresas_normalizadas = []
for i in range(len(empresas)):
    empresas_normalizadas += [normalizar_empresas(empresas[i])]