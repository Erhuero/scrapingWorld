describe('Create and mark-unmark as favorite', function () {

    Cypress.config('pageLoadTimeout', 10000)

    before(function () {
        cy.SignIn()
    })

    it('Create a post', function () {
        //cy.contains('New Post').click()//appuie sur le menu new post
        cy.get('ul.navbar-nav').children().contains('New Post').click() //ul est les caracteres a debut de la balise navbar est la balise a l'interieur
        //children permet d'avoir les balises contenues dans le navbar et on ajoute contains pour cliquer sur le texte New Post
        //l'acces se fait plus precisement
        cy.hash().should('include', '#/editor')//verifie qu'on est bien sur la bonne page, le hash url de la page activeS
        //cy.location('hash').should('include','#/editor') //même chose que la ligne precedente
        cy.get('form').within(($form) => {
            cy.get('input').first().type('Cheekiii breakiii')//trouve l'entree du titre et marque le message
            cy.get('input').eq('1').type('Daym bro !')//slash inverse pour eviter l'apostrophe
            cy.get('textarea').last().type('Fucking bourbier around here bruh')
            cy.get('input[placeholder="Enter tags"]').type("daym")
            cy.get('.btn').contains('Publish Article').click()
            //utilisation des index pour retrouver les bonnes balises : first, eq () et last
        })

        cy.url().should('include', 'article')//pas besoin de hastag avec url(), retourne l'url complet
    })
    
    it('Mark-unmark as favorite', function () {
        //cy.get('.nav-link').contains('Rastanx').click()//clique sur le bouton correspondant
        cy.get('ul.navbar-nav').children().contains('Rastanx').click()
        cy.contains('My Articles').should('be.visible')
        cy.get('.ion-heart').first().click()//clique sur l'artcle favori
        cy.contains('Favorited Articles').click()
        cy.url().should('include', 'favorites')
        //cy.get('.ion-heart', {timeout:10000}).first().click()//clique sur l'artcle favori
        cy.reload()//recharge la page
        cy.contains('No articles are here... yet.').should('be.visible')
        cy.go('back')
        //cy.go(-1)//aller en arriere
        //cy.go('forward')//aller en avant
        //cy.go(1)//aller en avant autrement
    })
})