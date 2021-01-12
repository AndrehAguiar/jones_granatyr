CREATE DEFINER=`root`@`localhost` FUNCTION `GetPeriodoCurso`(curso varchar(100)) RETURNS varchar(100) CHARSET utf8mb4
begin
	declare periodo varchar(100);
    if (curso = 'ENGENHARIA AGRONÔMICA' or 
		curso = 'ENSINO MÉDIO E TÉCNICO EM AGROPECUÁRIA' or
        curso = 'TÉCNICO EM AGROPECUÁRIA' or
        curso = 'ENSINO MÉDIO E TÉCNICO EM INFORMÁTICA' or
        curso = 'ENSINO MÉDIO E TÉCNICO EM ALIMENTOS') then
	  set periodo = 'INTEGRAL';
      
	elseif (curso = 'TÉCNICO EM INFORMÁTICA - NOTURNO' or 
			curso = 'CIÊNCIA DA COMPUTAÇÃO - BACHARELADO' or
			curso = 'CIÊNCIAS BIOLÓGICAS - LICENCIATURA' or
			curso = 'EDUCAÇÃO FÍSICA - BACHARELADO - NOTURNO' or
			curso = 'TÉCNICO EM MEIO AMBIENTE' or
            curso = 'TÉCNICO EM ENFERMAGEM - NOTURNO' or
            curso = 'EDUCAÇÃO FÍSICA - LICENCIATURA - NOTURNO' or
            curso = 'TÉCNICO EM SEGURANÇA DO TRABALHO') then
     set periodo = 'NOTURNO';
	
    elseif (curso = 'EDUCAÇÃO FÍSICA - LICENCIATURA - VESPERTINO' or
            curso = 'TÉCNICO EM INFORMÁTICA - VESPERTINO' or
            curso = 'EDUCAÇÃO FÍSICA - BACHARELADO - VESPERTINO') then
	  set periodo = 'VESPERTINO';
	
    end if;  
	return periodo;
end