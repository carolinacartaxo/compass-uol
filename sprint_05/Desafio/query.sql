SELECT COALESCE(
    SUM(
        CASE 
            WHEN REGIAO_BENEFICIARIO = 'NORDESTE'
                 AND BENEFICIARIO_DEFICIENTE_FISICO = 'N' 
                 AND RACA_BENEFICIARIO = 'Parda' OR RACA_BENEFICIARIO = 'Preta' 
            THEN DATE_DIFF('year', TO_TIMESTAMP(DATA_NASCIMENTO, 'dd/MM/yyyy'), UTCNOW()) 
            ELSE 0 
        END
    ) 
    / NULLIF(
        SUM(
            CASE 
                WHEN REGIAO_BENEFICIARIO = 'NORDESTE' 
                     AND BENEFICIARIO_DEFICIENTE_FISICO = 'N' 
                     AND RACA_BENEFICIARIO = 'Parda' OR RACA_BENEFICIARIO = 'Preta'
                THEN 1 
                ELSE 0 
            END
        ), 
        0
    ), 
    0
) AS MEDIA_IDADE 
FROM S3Object s 
WHERE REGIAO_BENEFICIARIO = 'NORDESTE' 
  AND BENEFICIARIO_DEFICIENTE_FISICO = 'N' 
  AND UPPER(MODALIDADE_ENSINO_BOLSA) = 'PRESENCIAL'
  AND RACA_BENEFICIARIO = 'Parda' OR RACA_BENEFICIARIO = 'Preta'