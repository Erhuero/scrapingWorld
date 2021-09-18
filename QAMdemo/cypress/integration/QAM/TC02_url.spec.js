describe('Create and mark-unmark as favorite',  function (){
    it('Sign in', function () {
        cy.visit('https://react-redux.realworld.io/#/login')//lance le programme
        cy.title().should('eq', 'Conduit')//nous donne le titre et verifie si il est correct
        cy.location('protocol').should('eq','https:')//verifie si l'addresse est bien en https
        cy.get('input[type="email"]').type('constantin.chtanko@gmail.com')
        cy.get('input[type="password"]').type('Osmium.222')
        cy.get('.btn').contains('Sign in').should('be.visible').click() //should ajoute un message dans les logs
        // .btn fait reference au bouton d'inscription
        cy.contains('Your Feed', {timeout:10000}).should('be.visible')//verifie si le mot Your Feed est bien present sur la page
        //timeout laisse la page pendant quelques secondes et vérifie si le mot Your Feed existe bien
    })

    it('Create a post', function() {
        cy.contains('New Post').click()//appuie sur le menu new post
        cy.hash().should('include','#/editor')//verifie qu'on est bien sur la bonne page, le hash url de la page activeS
        //cy.location('hash').should('include','#/editor') //même chose que la ligne precedente
        cy.get('input[placeholder="Article Title"]').type('Cheekiii breakiii')//trouve l'entree du titre et marque le message
        cy.get('input[placeholder="What\'s this article about?"]').type('Daym bro !')//slash inverse pour eviter l'apostrophe
        cy.get('textarea[placeholder="Write your article (in markdown)"]').type('Fucking bourbier around here bruh')
        cy.get('input[placeholder="Enter tags"]').type("daym")
        cy.get('.btn').contains('Publish Article').click()
        cy.url().should('include','article')//pas besoin de hastag avec url(), retourne l'url complet
    })

    it('Mark-unmark as favorite', function () {
        cy.get('.nav-link').contains('Rastanx').click()//clique sur le bouton correspondant
        cy.contains('My Articles').should('be.visible')
        cy.get('.ion-heart').click()//clique sur l'artcle favori
        cy.contains('Favorited Articles').click()
        cy.url().should('include','favorites')
        cy.get('.ion-heart').click()//clique sur l'artcle favori
        cy.reload()//recharge la page
        cy.contains('No articles are here... yet.').should('be.visible')
        cy.go('back')
        //cy.go(-1)//aller en arriere
        //cy.go('forward')//aller en avant
        //cy.go(1)//aller en avant autrement
    })
})