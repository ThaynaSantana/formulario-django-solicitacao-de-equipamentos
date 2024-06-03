function enviarEmail() {
    // Pegando os dados do recibo
    var form = document.getElementsByName('form');
    var solicitante = form.solicitante.textContent;
    var inicio_colaborador = form.inicio_colaborador.textContent;
    var nome = form.nome.textContent;
    var endereco = form.endereco.textContent;
    var criacao_email = form.criacao_email.textContent;
    var gestor_direto = form.gestor_direto.textContent;
    var cargo = form.cargo.textContent;
    var departamento = form.departamento.textContent;
    var cliente = form.cliente.textContent;
    var dispositivo = form.dispositivo.textContent;
    var codigo_ativo = form.codigo_ativo.textContent;

    var assunto = encodeURIComponent("Pedido de Solicitação de Equipamento para Novo Colaborador");
    var from = "suporte@luminiitisolutions.com";
    // var cc = "isabely@luminiitisolutions.com"
    var corpo = encodeURIComponent(`
    Prezado,\n
    Solicito um equipamento para novo colaborador, para mais informações veja na planilha de Solicitações.xlsx <a href="https://www.google.com">Clique Aqui</a>.\n\n
    <table border="1">
        <tr><th>Solicitante</th><td>${solicitante}</td></tr>
        <tr><th>Início do Colaborador</th><td>${inicio_colaborador}</td></tr>
        <tr><th>Nome</th><td>${nome}</td></tr>
        <tr><th>Endereço</th><td>${endereco}</td></tr>
        <tr><th>Criação de Email</th><td>${criacao_email}</td></tr>
        <tr><th>Gestor Direto</th><td>${gestor_direto}</td></tr>
        <tr><th>Cargo</th><td>${cargo}</td></tr>
        <tr><th>Departamento</th><td>${departamento}</td></tr>
        <tr><th>Cliente</th><td>${cliente}</td></tr>
        <tr><th>Dispositivo</th><td>${dispositivo}</td></tr>
        <tr><th>Código do Ativo</th><td>${codigo_ativo}</td></tr>
    </table>
    `);
    // Montagem do email
    var link = "mailto:" + from + "?subject=" + assunto + "&body=" + corpo;
    // Abre o cliente de e-mail padrão do usuário, provavelmente Outlook.
    window.location.href = link;
}