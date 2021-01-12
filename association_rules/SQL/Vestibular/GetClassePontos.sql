CREATE DEFINER=`root`@`localhost` FUNCTION `GetClassePontos`(pontos float) RETURNS varchar(20) CHARSET utf8mb4
begin
	declare faixa varchar(20);
    if (pontos < 20) then
		set faixa = 'menos 20 pontos';
	elseif (pontos >= 20 and pontos <= 39) then
		set faixa = '20-40 pontos';
	elseif (pontos >= 40 and pontos <= 60) then
		set faixa = '40-60 pontos';
	elseif (pontos >= 60 and pontos <= 80) then
		set faixa = '60-80 pontos';
	else
		set faixa = 'acima 80 pontos';
	end if;
    
    return faixa;
end