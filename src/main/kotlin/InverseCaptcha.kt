/**
 * @author Jan De Schryver <Jan.DeSchryver@bucephalus.be>
 */
// 1 december 2018

fun decodeCaptcha(captcha: String) =
        captcha.filterIndexed({i, c -> captcha[(i+1)%captcha.length] == c})
                .sumBy { it.toRealInt() }

fun decodeCaptcha2(captcha: String, l: Int = captcha.length/2) =
        captcha.filterIndexed({i, c -> captcha[(i+l)%captcha.length] == c})
                .sumBy { it.toRealInt() }

fun Char.toRealInt() = this.toInt() - 48

fun main(args:Array<String>) {
    val captcha = "111233"
    println(decodeCaptcha(captcha))
    println(decodeCaptcha2(captcha))
}