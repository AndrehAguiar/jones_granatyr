CREATE DEFINER=`root`@`localhost` FUNCTION `GetDiaSemana`(data_pedido date) RETURNS varchar(10) CHARSET utf8mb4
begin
	set lc_time_names = 'pt_BR';
	return dayname(data_pedido);
end