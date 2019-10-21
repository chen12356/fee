//保存成功的提示信息
function showResult() {
    showResultDiv(true);
    window.setTimeout("showResultDiv(false);", 3000);
}

function showResultDiv(flag) {
    var divResult = document.getElementById("save_result_info");
    if (flag)
        divResult.style.display = "block";
    else
        divResult.style.display = "none";
}

//显示修改密码的信息项
function showPwd(chkObj) {
    if (chkObj.checked)
        document.getElementById("divPwds").style.display = "block";
    else
        document.getElementById("divPwds").style.display = "none";
}

$(function () {
    $('#fee').click(function () {
        window.open('/tariffApp/feeList/', target = '_self');
    });

    $('#service').click(function () {
        window.open('/serviceApp/serviceList/', target = '_self');
    });
});