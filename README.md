# Cálculo de paneles que caben en un techo

Este proyecto plantea una solución para calcular la **cantidad máxima de paneles rectangulares** que pueden colocarse dentro de un **techo rectangular**.

La idea principal es fijar las **dimensiones del techo** y evaluar distintas **orientaciones de los paneles**, aplicando recursión.

---

## Lógica de la solución

El algoritmo considera **dos casos**, según la orientación de los paneles:

### Caso 1: Orientación vertical
- Los paneles se colocan en orientación vertical.
- Se calcula cuántos paneles caben en **filas** y **columnas**, formando una matriz.
- Al colocar esta matriz, queda un área rectangular sobrante.
- Se selecciona el **mayor de los rectángulos restantes** y se aplica el algoritmo de forma recursiva sobre dicho espacio.

### Caso 2: Orientación horizontal
- Los paneles se colocan en orientación horizontal.
- Se calcula cuántos paneles caben en filas y columnas para esta orientación.
- Al igual que en el caso anterior, se identifica el mayor rectángulo sobrante.
- El algoritmo se aplica recursivamente sobre ese espacio restante.

---

## Caso base

La recursión  continúa hasta que **no es posible colocar ningún panel adicional**, es decir, el rectangulo del techo sea menor al del panel.  
Este escenario se utiliza como **caso base** de la recursión.

---

## Resultado final

El algoritmo evalúa ambos casos (orientación vertical y horizontal) y retorna el **máximo número de paneles** que pueden colocarse dentro del techo.

---
## Implementación del bonus: paneles en un triángulo isósceles

En un inicio se evaluó la posibilidad de utilizar el **teorema de Pitágoras** para determinar hasta qué punto era posible colocar un panel hacia los extremos del triángulo. Sin embargo, se necesitaba tener más de un valor de los lados del triángulo, y en este caso solo se tenía un cateto, por lo que no se pudo aplicar pitágoras.

Luego me di cuenta que se podía aplicar el **Teorema de Tales** y con esto obtuve el valor en donde se puede colocar el panel lo mas a la izquerda posible.

Con esto ya obtenemos el espacio en donde si pueden colocarse los paneles, el espacio se calcula asi:
- espacio =  base - 2x, siendo x el valor en donde no pueden ir rectángulos

Una vez calculada esta nueva base, se determina cuántos paneles caben en dicha capa y se aplica el algoritmo de forma recursiva sobre el **triángulo superior restante**. En cada iteración, el triángulo se va reduciendo (por ejemplo, la base pasa a ser `base - 4x`, y así sucesivamente), hasta que no es posible colocar ningún panel adicional.

Este procedimiento se evalúa considerando ambas orientaciones tanto en horizontal como vertical, y finalmente se selecciona el **mayor contador obtenido** entre ambos.

---


## Link al video


## Ejecución del código

Para ejecutar el proyecto, sigue estos pasos desde la raíz del repositorio:

```bash
cd python
python3 main.py
