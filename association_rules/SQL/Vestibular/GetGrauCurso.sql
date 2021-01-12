CREATE DEFINER=`root`@`localhost` FUNCTION `GetGrauCurso`(curso varchar(100)) RETURNS varchar(100) CHARSET utf8mb4
begin
	declare grau varchar(100);
    if (curso = 'ENGENHARIA AGRONÔMICA' or 
		curso = 'CIÊNCIA DA COMPUTAÇÃO - BACHARELADO') then
	  set grau = 'SUPERIOR';
      
	elseif (curso = 'ENSINO MÉDIO E TÉCNICO EM AGROPECUÁRIA' or 
			curso = 'ENSINO MÉDIO E TÉCNICO EM INFORMÁTICA' or
			curso = 'ENSINO MÉDIO E TÉCNICO EM ALIMENTOS') then
     set grau = 'ENSINO MÉDIO E TÉCNICO';
	
    elseif (curso = 'TÉCNICO EM INFORMÁTICA - NOTURNO' or
            curso = 'TÉCNICO EM AGROPECUÁRIA' or
            curso = 'TÉCNICO EM INFORMÁTICA - VESPERTINO' or
            curso = 'TÉCNICO EM MEIO AMBIENTE' or
            curso = 'TÉCNICO EM ENFERMAGEM - NOTURNO' or
            curso = 'TÉCNICO EM SEGURANÇA DO TRABALHO') then
	  set grau = 'TÉCNICO';
	
    elseif (curso = 'CIÊNCIAS BIOLÓGICAS - LICENCIATURA' or 
			curso = 'EDUCAÇÃO FÍSICA - LICENCIATURA - VESPERTINO' or
			curso = 'EDUCAÇÃO FÍSICA - LICENCIATURA - NOTURNO') then
     set grau = 'LICENCIATURA';
     
     elseif (curso = 'EDUCAÇÃO FÍSICA - BACHARELADO - NOTURNO' or 
			curso = 'EDUCAÇÃO FÍSICA - BACHARELADO - VESPERTINO') then
     set grau = 'BACHARELADO';
    
    end if;  
	return grau;
end