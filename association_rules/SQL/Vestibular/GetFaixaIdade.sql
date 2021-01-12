CREATE DEFINER=`root`@`localhost` FUNCTION `GetFaixaIdade`(idade int) RETURNS varchar(20) CHARSET utf8mb4
begin
	declare faixa varchar(20);
    if (idade < 17) then
		set faixa = 'menor 17';
	elseif (idade = 17) then
		set faixa = '17 anos';
	elseif (idade > 17 and idade <= 22) then
		set faixa = 'entre 18 e 22';
	elseif (idade > 22 and idade <= 30) then
		set faixa = 'entre 23 e 30';
	elseif (idade > 30 and idade <= 40) then
		set faixa = 'entre 31 e 40';
	elseif (idade > 40) then
		set faixa = 'acima 40';
	end if;
    
    return faixa;
end