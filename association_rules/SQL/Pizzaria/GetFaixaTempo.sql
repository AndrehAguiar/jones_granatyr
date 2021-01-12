CREATE DEFINER=`root`@`localhost` FUNCTION `GetFaixaTempo`(minutos float) RETURNS varchar(10) CHARSET utf8mb4
begin
	declare faixa varchar(10);
    if (minutos >= 10 and minutos < 22) then
		set faixa = 'tp 10-22';
	elseif (minutos >= 22 and minutos < 33) then
		set faixa = 'tp 22-33';
	elseif (minutos >= 33 and minutos < 44) then
		set faixa = 'tp 33-44';
	elseif (minutos >= 44) then
		set faixa = 'tp 44-55';
	end if;
    
    return faixa;
end