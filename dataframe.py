import pandas as pd

df_csv = pd.read_csv('./data/attentions.csv', delimiter=';')

df_csv.rename(columns={
    'RUT AFP': 'rut_afp',
    'RUT DV AFP':'rut_dv_afp',
    'Periodo':'periodo',
    'Codigo Comuna':'codigo_comuna',
    'Identificador Agencia':'identificador_agencia',
    'RUT Agente':'rut_agente',
    'RUT DV Agente':'rut_dv_agente',
    'Numero Inscripcion':'numero_inscripcion',
    'Nombre Agente':'nombre_agente',
    'Apellido Paterno Agente':'apellido_paterno_agente',
    'Apellido Materno Agente':'apellido_materno_agente',
    'Fecha atencion':'fecha_atencion',
    'Tipo Atencion':'tipo_atencion',
    'Hora Inicio Espera':'hora_inicio_espera',
    'Hora Termino Espera':'hora_termino_espera',
    'Tiempo de Espera':'tiempo_espera',
    'Hora Inicio Atencion':'hora_inicio_atencion',
    'Hora Termino Atencion':'hora_termino_atencion',
    'Tiempo de Atencion':'tiempo_atencion',
    'RUT Afiliado':'rut_afiliado',
    'RUT DV Afiliado':'rut_dv_afiliado'
    }, inplace=True)

df_csv.to_csv('./clean_data/data.csv', index=False)

print(df_csv)