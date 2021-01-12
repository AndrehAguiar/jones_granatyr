CREATE DEFINER=`root`@`localhost` FUNCTION `GetFaixaValor`(valor_total float) RETURNS varchar(10) CHARSET utf8mb4
begin
	declare faixa varchar(10);
	if (valor_total >= 10 and valor_total < 14) then
		set faixa = 'vl 10-14';
	elseif (valor_total >= 14 and valor_total < 18) then
		set faixa = 'vl 14-18';
	elseif (valor_total >= 18 and valor_total < 22) then
		set faixa = 'vl 18-22';
	elseif (valor_total >= 22 and valor_total < 26) then
		set faixa = 'vl 22-26';
	elseif (valor_total >= 26 and valor_total < 30) then
		set faixa = 'vl 26-30';
	elseif (valor_total >= 30 and valor_total < 34) then
		set faixa = 'vl 30-34';
	elseif (valor_total >= 34 and valor_total < 38) then
		set faixa = 'vl 34-38';
	elseif (valor_total >= 38 and valor_total < 42) then
		set faixa = 'vl 38-42';
	elseif (valor_total >= 42 and valor_total < 46) then
		set faixa = 'vl 42-46';
	elseif (valor_total >= 46) then
		set faixa = 'vl 46-50';
	end if;

	return faixa;
end