CREATE DEFINER=`root`@`localhost` FUNCTION `GetPeriodoVenda`(hora_pedido time) RETURNS varchar(10) CHARSET utf8mb4
begin
	declare periodo varchar(10);
    if (hora_pedido < '20:00:00') then
		set periodo = 'Inicio';
	elseif (hora_pedido >= '20:00:00' and hora_pedido < '22:00:00') then
		set periodo = 'Pico';
	elseif (hora_pedido >= '22:00:00') then
		set periodo = 'Final';
	end if;
    return periodo;
end