VARIABLES = [
    'idade',
    'sexo',
    'scv___1',
    'scv___2',
    'scv___3',
    'scv___4',
    'scv___5',
    'scv___6',
    'sr___1',
    'sr___2',
    'sr___3',
    'dm___1',
    'dm___2',
    'comorb_outras___1',
    'comorb_outras___3',
    'comorb_outras___4',
    'comorb_outras___5',
    'comorb_outras___6',
    'comorb_outras___8',
    'comorb_outras_dialise',
    'med_domiciliar___3',
    'med_domiciliar___6',
    'med_domiciliar___7',
    'med_domiciliar___13',
    'hv___1',
    'hv___2',
    'hv___3',
    'hv___4',
    'glasgow_menor15_adm_final',
    'fc_adm_final',
    'fr_adm_final',
    'temp_adm_final',
    'sat_fio2',
    'vm_adm_final',
    'hb_adm_final',
    'leucocitos_adm_final',
    'neutrofilos_adm_final',
    'linfocitos_adm_final',
    'plaquetas_adm_final',
    'bb_total_adm_final',
    'creatinina_adm_final',
    'ferritina_adm_final',
    'lactato_adm_final_padrao',
    'pcr_adm_final',
    'sodio_adm_final',
    'ast_alt',
    'ureia_adm_final',
    'ph_adm_final',
    'pco2_adm_final',
    'bicarbonato_adm_final',
    'troponina_adm_final_prop',
    'po2_fio2_adm_final',
    'pasamina90',
    'padamina60',
    'vacina',
    'vacina_doses',

    ################### SOCIODEMOGRAPHIC VARIABLES ###################
    'Hometown_GDP',
    'Hometown_DHI',
    'Hospital_GDP',
    'Hospital_DHI',
    'Academic_status',
    'Accreditation',
    'Source_of_income',
    ################### SOCIODEMOGRAPHIC VARIABLES ###################

    'direto_cti', # Exclude from the classification step, variable used to preprocess the dataset.
    'dataadm',    # Exclude from the classification step, variable used to preprocess the dataset.
    'onda',        # Exclude from the classification step, variable used to preprocess the dataset.

    'intercorrencia___13',
    'intercorrencia___3',
    'intercorrencia___16',
    'intercorrencia___6',
    'intercorrencia___5',
]

SOCIODEMOGRAPHIC_VARIABLES = [
    'Hometown_GDP',
    'Hometown_DHI',
    'Hospital_GDP',
    'Hospital_DHI',
    'Academic_status',
    'Accreditation',
    'Source_of_income',
]

OUTCOMES = [
    'intercorrencia_3_5_6_13_16',
]

COLUMNS_TO_EXCLUDE_BY_OUTCOME = {
    'intercorrencia_3_5_6_13_16': ['intercorrencia___3', 'intercorrencia___13', 'intercorrencia___6', 'intercorrencia___16', 'intercorrencia___5'],
}

VARIABLES_TO_RENAME_SOCIODEMOGRAPHIC = {
    'idade' : 'Age',
    'ureia_adm_final' : 'Urea',
    'plaquetas_adm_final' : 'Platelets',
    'sat_fio2' : r'SatO$_2$/FiO$_2$',
    'scv___3' : 'Heart failure',
    'fr_adm_final' : 'Respiratory rate',
    'po2_fio2_adm_final' : r'pO$_2$/FiO$_2$',    
    'Hospital_GDP' : 'Hospital GDP',
    'Hometown_GDP' : 'Hometown GDP',
}

VARIABLES_TO_RENAME_NO_SOCIODEMOGRAPHIC = {
    'idade' : 'Age',
    'ureia_adm_final' : 'Urea',
    'sat_fio2' : r'SatO$_2$/FiO$_2$',
    'plaquetas_adm_final' : 'Platelets',
    'scv___1' : 'Arterial hypertension',
    'pco2_adm_final': r'Arterial pCO$_2$',
    'fr_adm_final' : 'Respiratory rate',
    'po2_fio2_adm_final' : r'pO$_2$/FiO$_2$',
    'scv___3' : 'Heart failure',
}
