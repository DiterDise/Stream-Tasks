function atm(value) {
    let diff = 0;
    let nominals = [200, 100, 50, 20, 10];
    let sum = nominals.reduce(function(sum, elem) {
    	return sum + elem * 10;
    }, 0);
    let resultStr = "";
    nominals.forEach((nominal) => {
        sum -= nominal * 10;
        diff = Math.max(value - sum, 0);
        let nominal_count = Math.trunc(diff / nominal) + (diff % nominal != 0);
        value -= nominal_count*nominal;
        resultStr += nominal + " = " + nominal_count + ", ";
    });
    console.log(resultStr);
}
atm(340)