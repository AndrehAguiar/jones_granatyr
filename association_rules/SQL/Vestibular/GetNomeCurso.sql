CREATE DEFINER=`root`@`localhost` FUNCTION `GetNomeCurso`(curso varchar(100)) RETURNS varchar(100) CHARSET utf8mb4
begin
	declare novocurso varchar(100);
        if (curso = 'ENGENHARIA AGRONÔMICA') then
      set novocurso = 'ENGENHARIA AGRONÔMICA';
	elseif (curso = 'ENSINO MÉDIO E TÉCNICO EM AGROPECUÁRIA') then
      set novocurso = 'ENSINO MÉDIO E TÉCNICO EM AGROPECUÁRIA INTEGRADO';
	elseif (curso = 'TÉCNICO EM INFORMÁTICA - NOTURNO' or 
			curso = 'TÉCNICO EM INFORMÁTICA - VESPERTINO') then
	  set novocurso = 'INFORMÁTICA';
	elseif (curso = 'TÉCNICO EM AGROPECUÁRIA') then
      set novocurso = 'AGROPECUÁRIA';
	elseif (curso = 'CIÊNCIA DA COMPUTAÇÃO - BACHARELADO') then
      set novocurso = 'CIÊNCIA DA COMPUTAÇÃO';
	elseif (curso = 'ENSINO MÉDIO E TÉCNICO EM INFORMÁTICA') then
      set novocurso = 'ENSINO MÉDIO E TÉCNICO EM INFORMÁTICA';
	elseif (curso = 'CIÊNCIAS BIOLÓGICAS - LICENCIATURA') then
      set novocurso = 'CIÊNCIAS BIOLÓGICAS';
	elseif (curso = 'EDUCAÇÃO FÍSICA - LICENCIATURA - VESPERTINO' or
            curso = 'EDUCAÇÃO FÍSICA - BACHARELADO - NOTURNO' or
            curso = 'EDUCAÇÃO FÍSICA - LICENCIATURA - NOTURNO' or
            curso = 'EDUCAÇÃO FÍSICA - BACHARELADO - VESPERTINO') then
	  set novocurso = 'EDUCAÇÃO FÍSICA';
	elseif (curso = 'TÉCNICO EM MEIO AMBIENTE') then
      set novocurso = 'MEIO AMBIENTE';
	elseif (curso = 'TÉCNICO EM ENFERMAGEM - NOTURNO') then
      set novocurso = 'ENFERMAGEM';
	elseif (curso = 'ENSINO MÉDIO E TÉCNICO EM ALIMENTOS') then
      set novocurso = 'ENSINO MÉDIO E TÉCNICO EM ALIMENTOS';
	elseif (curso = 'TÉCNICO EM SEGURANÇA DO TRABALHO') then
      set novocurso = 'SEGURANÇA DO TRABALHO';
    end if;  
    
	return novocurso;
end