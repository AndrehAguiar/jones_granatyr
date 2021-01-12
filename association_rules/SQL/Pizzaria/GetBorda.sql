CREATE DEFINER=`root`@`localhost` FUNCTION `GetBorda`(valor_borda float) RETURNS varchar(10) CHARSET utf8mb4
begin
	declare borda varchar(10);
    if (valor_borda > 0) then
		set borda = 'Borda sim';
    else
		set borda = 'Borda não';
	end if;
    
    return borda;
    
end