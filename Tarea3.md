
# Tarea 3

### Ejercicio 1

El gremio que agrupa a los obreros de establecimientos industriales relacionados con Alimentación y Bebidas, después de llevar a cabo una investigación llega a la conclusión de que el sueldo promedio pagado por las empresas del sector, es de \\$ 25 la hora con una desviación estándar de \\$ 3. Una empresa cervecera belga se ha instalado en el país desde hace 3 meses, contratando a 120 obreros. Por averiguaciones realizadas dentro de la planta se conoce que el sueldo promedio pagado es de \\$ 30 la hora. ¿Podrán sostener los afiliados al gremio que el sueldo promedio que paga la empresa belga es superior al negociado por el sector industrial correspondiente?


```R
mu <- 25 #μ
S <- 3 #σ
n <- 120
x_barra <- 30

H0 <- "x_barra <= μ" # Sueldo empresa belga es <= al sector industrial
print("H0: x_barra <= μ Sueldo empresa belga es <= al sector industrial")

H1 <- "x_barra > μ" #Sueldo empresa belga es > al sector industrial
print("H1: x_barra > μ Sueldo empresa belga es > al sector industrial")

# Usando un intervalo de confianza del 95%
z_tabla <- qnorm(.95)
print(paste("El z de tablas es: ", z_tabla))
z_calculado <- ( x_barra - mu ) / ( S / sqrt(n) )
print(paste("El z calculado es: ", z_calculado))

if (z_calculado > z_tabla){
    print("H0 se rechaza")
    print("Hay evidencia estadisticamente significativa como para rechazar la hipótesis nula")
    print("Por tanto se puede afirmar que la empresa belga paga mejor otras empresas del sector")    
}
```

    [1] "H0: x_barra <= <U+03BC> Sueldo empresa belga es <= al sector industrial"
    [1] "H1: x_barra > <U+03BC> Sueldo empresa belga es > al sector industrial"
    [1] "El z de tablas es:  1.64485362695147"
    [1] "El z calculado es:  18.2574185835055"
    [1] "H0 se rechaza"
    [1] "Hay evidencia estadisticamente significativa como para rechazar la hipótesis nula"
    [1] "Por tanto se puede afirmar que la empresa belga paga mejor otras empresas del sector"


### Ejercicio 2

Una empresa que fabrica automóviles, trabaja en un modelo en el que la especificación de los frenos expresa que la distancia requerida para parar cuando el auto marcha a una velocidad de 160 Km. por hora, es de 10 metros. El Departamento de Investigación y Desarrollo ha efectuado una innovación en el sistema de frenos de dicho modelo y establece que la nueva distancia requerida para frenar es menor que la que se venía especificando. Para corroborar esta aseveración, se toma una muestra de 10 automóviles a los cuales se les coloca el nuevo sistema de frenos. Se los lleva a la sección de pruebas donde se los hace marchar a 160 Km. por hora, registrándose para cada auto la distancia requerida para parar luego de aplicar el freno a fondo.

Los resultados obtenidos fueron:

| Auto No. | Distancia |
|:--------:|:---------:|
|     1    |     7     |
|     2    |     5     |
|     3    |     6     |
|     4    |     5     |
|     5    |     6     |
|     6    |     9     |
|     7    |     8     |
|     8    |     8     |
|     9    |     7     |
|    10    |     9     |

¿Qué puede decir de la aseveración del Departamento de Investigación y Desarrollo, en base a la evidencia presentada por la prueba del nuevo dispositivo de frenos? 


```R
mu <- 10
todas_distancias <- c(7, 5, 6, 5, 6, 9, 8, 8, 7, 9)
x_barra <- mean(todas_distancias)
s <- sd(todas_distancias)
n <- length(todas_distancias)

H0 <- "x_barra >= μ" # La prueba del departamento de investigación muestra que el nuevo dispositivo no es 
# mejor que el anterior
print("H0: x_barra <= μ Distancia frenado >= al dispositivo previo")

H1 <- "x_barra < μ" #Distancia frenado es > al sector industrial
print("H1: x_barra > μ Distancia frenado es > al dispositivo previo")

t_tabla <- qt(.05, df = n-1)
print(paste("El t de tablas es: ", t_tabla))
t_calculado <- ( x_barra - mu ) / ( s / sqrt(n-1) )
print(paste("El t calculado es: ", t_calculado))

if (t_calculado < t_tabla){
    print("H0 se rechaza")
    print("Hay evidencia estadisticamente significativa como para rechazar la hipótesis nula")
    print("Por tanto se puede afirmar que el nuevo dispositivo reduce las distancias de frenado")    
}
```

    [1] "H0: x_barra <= <U+03BC> Distancia frenado >= al dispositivo previo"
    [1] "H1: x_barra > <U+03BC> Distancia frenado es > al dispositivo previo"
    [1] "El t de tablas es:  -1.83311293265624"
    [1] "El t calculado es:  -6.03738353924943"
    [1] "H0 se rechaza"
    [1] "Hay evidencia estadisticamente significativa como para rechazar la hipótesis nula"
    [1] "Por tanto se puede afirmar que el nuevo dispositivo reduce las distancias de frenado"


### Ejercicio 3

De acuerdo a trabajos de marketing ya realizados, se piensa que el 30% de las personas que habitualmente sale a comer a restaurantes por lo menos una vez por semana, eligen un determinado comercio en función del precio de los servicios ofrecidos. Un grupo inversor desea montar una cadena de restaurantes utilizando la calidad de los alimentos ofrecidos como publicidad para penetrar en mercado. Para estar seguros de que el precio no será un factor fundamental en la competencia, encarga a una empresa de encuestas de opinión, investigar sobre el tema. 
 
La empresa decide tomar una muestra aleatoria de 100 personas que ingresan a restaurantes cuidadosamente seleccionados; una de las preguntas de la entrevista estaba referida a la importancia del precio del servicio en la elección del local. Luego de sistematizar la información obtenida en la muestra, se observó que el 38% de los encuestados consideraba al precio como el factor preponderante en la elección. ¿Convalida este resultado muestral la creencia generalizada en el marketing con respecto a las motivaciones de los concurrentes a comedores?


```R
P <- .30
Q <- 1-P
n <- 100
p <- .38
q <- 1-p


H0 <- "p <= P" # La proporción de los comenzales encuestados por la empresa que consideran el precio
# importante es menor o igual a los comenzales entrevistados anteriormente
print("H0: p <= P La proporción de la encuesta es menor o igual a la poporción de la población")

H1 <- "p > P" # La proporción de los comenzales encuestados por la empresa que consideran el precio
# importante es mayor a los comenzales entrevistados anteriormente
print("H1: p > P La proporción de la encuesta es mayor a la poporción de la población")

z_tabla <- qnorm(.95)
print(paste("El z de tablas es: ", z_tabla))
z_calculado <- (p - P) / sqrt ( (P * Q) / n)
print(paste("El z calculado es: ", z_calculado))
if (z_calculado > z_tabla){
    print("H0 se rechaza")
    print("Hay evidencia estadisticamente significativa como para rechazar la hipótesis nula")
    print("Por tanto se puede afirmar que los comenzales consideran importante el precio")    
}
```

    [1] "H0: p <= P La proporción de la encuesta es menor o igual a la poporción de la población"
    [1] "H1: p > P La proporción de la encuesta es mayor a la poporción de la población"
    [1] "El z de tablas es:  1.64485362695147"
    [1] "El z calculado es:  1.74574312188794"
    [1] "H0 se rechaza"
    [1] "Hay evidencia estadisticamente significativa como para rechazar la hipótesis nula"
    [1] "Por tanto se puede afirmar que los comenzales consideran importante el precio"


### Ejercicio 4

Una empresa telefónica ha realizado un estudio para ver la proporción de usuarios que se comunican a Internet a través de su línea telefónica. Para ello definió 2 estratos de clientes, los que gastan hasta \\$ 100 mensuales por el servicio de telefonía y los que gastan más de $ 100. En el primer estrato, compuesto por 326 usuarios, el 40% se conecta a Internet por medio de su línea telefónica y en el segundo estrato, compuesto por 136 clientes, el 59% se conectan por este medio. ¿Existe una suficiente evidencia de que la proporción de usuarios que se conectan a Internet por la línea telefónica es diferente en los dos estratos?


```R
n_100 <- 316
p_100 <- .40
q_100 <- 1 - p_100
n_mas_100 <- 136
p_mas_100 <- .59
q_mas_100 <- 1 - p_mas_100


H0 <- "P100 - P_mas_100 = 0" # La proporción de los usuarios que se comunican por internet son iguales
# iguales en los dos estratos
print("H0: P100 - P_mas_100 = 0 Es decir que la proporción de los dos estratos es igual")

H1 <- "P100 - P_mas_100 <> 0" # La proporción de los usuarios que se comunican por internet NO son iguales
# iguales en los dos estratos
print("H1: P100 - P_mas_100 <> 0 Es decir que la proporción de los dos estratos es diferente")

# Como no se tienen las proporciones poblacionales, y por la hipótesis nula tenemos que las proporciones
# son iguales, entonces P_100 - P_mas_100 = 0; además como las muestras son grandes, se supone que P = p

z_tabla_menor <- qnorm(.025)
print(paste("El z de tablas .025 es: ", z_tabla_menor))
z_tabla_mayor <- qnorm(.975)
print(paste("El z de tablas .975 es: ", z_tabla_mayor))
z_calculado <-( p_100 - p_mas_100 ) / sqrt(
            (
                (p_100 * q_100)
                / n_100
            )
            + 
            (
                (p_mas_100 * q_mas_100) / n_mas_100
            )
        )
print(paste("El z calculado es: ", z_calculado))

if ((z_calculado < z_tabla_menor) || (z_calculado > z_tabla_mayor)) {
    print("H0 se rechaza")
    print("Hay evidencia estadisticamente significativa como para rechazar la hipótesis nula")
    print("Por se puede afirmar que las proporciones de los estratos de usuarios son iguales entre si")    
}
```

    [1] "H0: P100 - P_mas_100 = 0 Es decir que la proporción de los dos estratos es igual"
    [1] "H1: P100 - P_mas_100 <> 0 Es decir que la proporción de los dos estratos es diferente"
    [1] "El z de tablas .025 es:  -1.95996398454005"
    [1] "El z de tablas .975 es:  1.95996398454005"
    [1] "El z calculado es:  -3.77131870845143"
    [1] "H0 se rechaza"
    [1] "Hay evidencia estadisticamente significativa como para rechazar la hipótesis nula"
    [1] "Por se puede afirmar que las proporciones de los estratos de usuarios son iguales entre si"


### Ejercicio 5

Una agencia de publicidad desea investigar si existen diferencias en cuanto al recuerdo de un cierto anuncio publicitario, cuando se utiliza la prensa escrita y la televisión. Para ello decide seleccionar una muestra de personas y entrevistarlas. Una vez resumidos los datos de la encuesta confecciona la siguiente tabla de distribución de frecuencias:

|                   -                  |      Medio     |    Medio   |
|:------------------------------------:|:--------------:|:----------:|
|                   -                  | Prensa Escrita | Television |
|  Cantidad de personas que recordaron |       25       |     10     |
|Cantidad de personas que no recordaron|       45       |     32     |


Pruebe la hipótesis de que la proporción de personas que recordaron el anuncio cuando apareció en la prensa es la misma que la proporción de personas que lo recordaron cuando lo vieron por televisión.


```R
pp <- 25/70
qp <- 1 - pp
pt <- 10/42
qt <- 1 - pt
np <- 70
nt <- 42

H0 <- "PP - PT = 0" # La proporción de las personas que recuerdan el anuncio en TV es diferente a
# la proporcion de las personas que recuerdan el anuncio en prensa
print("H0: PP - PT = 0 Es decir que la proporción de los dos medios es igual")

H1 <- "PP - PT <> 0" # La proporción de las personas que recuerdan el anuncio en TV es igual a
# la proporcion de las personas que recuerdan el anuncio en prensa
print("H1: PP - PT <> 0 Es decir que la proporción de los dos medios es diferente")

# Como no se tienen las proporciones poblacionales, y por la hipótesis nula tenemos que las proporciones
# son iguales, entonces PP - PT = 0; además como las muestras son grandes, se supone que P = p

z_tabla_menor <- qnorm(.025)
print(paste("El z de tablas .025 es: ", z_tabla_menor))
z_tabla_mayor <- qnorm(.975)
print(paste("El z de tablas .975 es: ", z_tabla_mayor))
z_calculado <-( pp - pt ) / sqrt(
            (
                (pp * qp)/np
            )
            + 
            (
                (pt * qt) / nt
            )
        )
print(paste("El z calculado es: ", z_calculado))

if ((z_calculado > z_tabla_menor) || (z_calculado < z_tabla_mayor)) {
    print("H0 no se rechaza")
    print("No hay evidencia estadisticamente significativa como para rechazar la hipótesis nula")
    print("Por tanto se puede afirmar que las proporciones de los dos medios son iguales")    
}
```

    [1] "H0: PP - PT = 0 Es decir que la proporción de los dos medios es igual"
    [1] "H1: PP - PT <> 0 Es decir que la proporción de los dos medios es diferente"
    [1] "El z de tablas .025 es:  -1.95996398454005"
    [1] "El z de tablas .975 es:  1.95996398454005"
    [1] "El z calculado es:  1.36565327993407"
    [1] "H0 no se rechaza"
    [1] "No hay evidencia estadisticamente significativa como para rechazar la hipótesis nula"
    [1] "Por tanto se puede afirmar que las proporciones de los dos medios son iguales"

