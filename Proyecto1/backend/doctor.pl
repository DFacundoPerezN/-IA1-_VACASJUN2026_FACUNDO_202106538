% modulo 
:- use_module(library(lists)).
% Hechos

:- multifile sintoma/1.

% Sintomas
sintoma(pantalla_negra).
sintoma(reinicio_inesperado).
sintoma(mensaje_de_error).
sintoma(lentitud_del_sistema).
sintoma(problema_arranque).
sintoma(pantalla_azul).
sintoma(pantalla_blanca).
sintoma(reinicio_bios).
sintoma(ruido_desconocido).
sintoma(temperatura_elevada).
sintoma(periferico_no_reconocido).
sintoma(sin_conexion_red).
sintoma(aplicacion_se_congela).
sintoma(bateria_no_carga).
sintoma(desconexion_usb_constante).

% --- Falla ---
:- multifile falla/1.

falla(sobrecalentamiento_procesador).
falla(disco_duro_lastimado).
falla(memoria_ram_defectuosa).
falla(fuente_poder_inestable).
falla(conflicto_drivers).
falla(malware).
falla(sector_arranque_corrupto).
falla(pasta_termica_seca).
falla(tarjeta_red_quemada).
falla(corto_circuito_usb).

% Recomendaciones
:- multifile recomendacion/1.

recomendacion(limpiar_ventiladores).
recomendacion(cambiar_pasta).
recomendacion(reemplazar_unidad_almacenamiento).
recomendacion(ejecutar_diagnostico_ram).
recomendacion(limpiar_contactos).
recomendacion(probar_otra_fuente_poder).
recomendacion(reinstalar_controladores).
recomendacion(analizar_sistema_con_antivirus).
recomendacion(reparar_inicio_desde_consola_sistema).
recomendacion(cambiar_tarjeta_red). 
recomendacion(usar_adaptador_usb).
recomendacion(desconectar_puertos_frontales).
recomendacion(actualizar_sistema_operativo).

% Reglas 

% getters
get_sintomas(Lista):- findall(Sintoma, sintoma(Sintoma), Lista).
get_fallas(Lista):- findall(Falla, falla(Falla), Lista).
get_recomendaciones(Lista):- findall(Recomendacion, recomendacion(Recomendacion), Lista).

% subset/2

% Relación: falla_causada_por(Falla, ListaDeSintomasRequeridos)
falla_causada_por(sobrecalentamiento_procesador, [temperatura_elevada, ruido_desconocido, reinicio_inesperado]).
falla_causada_por(disco_duro_lastimado, [lentitud_del_sistema, mensaje_de_error, ruido_desconocido]).
falla_causada_por(memoria_ram_defectuosa, [pantalla_azul, reinicio_inesperado, problema_arranque]).
falla_causada_por(fuente_poder_inestable, [reinicio_inesperado, reinicio_bios, pantalla_negra]).
falla_causada_por(malware, [lentitud_del_sistema, aplicacion_se_congela, mensaje_de_error]).
falla_causada_por(corto_circuito_usb, [desconexion_usb_constante, periferico_no_reconocido]).

% Regla principal para obtener el diagnóstico, solo devolverá la primera falla por el corte !
diagnosticar(ListaSintomasUsuario, Falla) :-
    falla_causada_por(Falla, SintomasRequeridos),
    subset(SintomasRequeridos, ListaSintomasUsuario), !.

% Relación: tratamiento(Falla, Recomendaciones)
tratamiento(sobrecalentamiento_procesador, [limpiar_ventiladores, cambiar_pasta]).
tratamiento(disco_duro_lastimado, [reemplazar_unidad_almacenamiento]).
tratamiento(memoria_ram_defectuosa, [ejecutar_diagnostico_ram, limpiar_contactos]).
tratamiento(fuente_poder_inestable, [probar_otra_fuente_poder]).
tratamiento(malware, [analizar_sistema_con_antivirus, actualizar_sistema_operativo]).
tratamiento(corto_circuito_usb, [desconectar_puertos_frontales]).

% Regla para obtener recomendaciones según síntomas
obtener_recomendaciones(ListaSintomasUsuario, Recomendaciones) :-
    diagnosticar(ListaSintomasUsuario, Falla),
    tratamiento(Falla, Recomendaciones).

% consult('doctor.pl').