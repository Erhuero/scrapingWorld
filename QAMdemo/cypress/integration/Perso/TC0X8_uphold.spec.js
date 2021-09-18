describe("Login", function () {
    Cypress.config('pageLoadTimeout', 10000)
    it('Sign in', function () {
        cy.visit('https://uphold.com/login')
        cy.get('input[name="username"]').type('constantin.chtanko@gmail.com')
        cy.get('input[name="password"]').type('Coch2024!')
        cy.get('.btn').contains('Sign in').should('be.visible').click()

            })
    it('Selectionner carte', function () {
      
        cy.get('.card').children().contains('Brave Browser').click()
        
    })
}) 