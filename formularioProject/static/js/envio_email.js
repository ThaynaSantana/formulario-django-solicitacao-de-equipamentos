function enviarEmail() {
    var assunto = encodeURIComponent("Pedido de Solicitação de Equipamento para Novo Colaborador");
    var from = "suporte@gmail.com";
    var corpo = encodeURIComponent("Prezado,\n Solicito um equipamento para novo colaborador, para mais informações veja na planilha de Solicitações.xlsx Localizada na Pasta Gente&Gestão/Pasta/Solicitações.xlsx.");
    // Montagem do email
    var link = "mailto:" + from + "?subject=" + assunto + "&body=" + corpo;

    // Abre o cliente de e-mail padrão do usuário, provavelmente Outlook.
    window.location.href = link;
}