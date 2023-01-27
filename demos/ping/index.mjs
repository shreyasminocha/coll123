import Koa from 'koa';
import Router from 'koa-router';

import { exec } from 'child_process';
import util from 'util';
const execp = util.promisify(exec);

const app = new Koa();
const router = new Router();

router.get('/', async (ctx) => {
	ctx.redirect('/ping?host=example.com');
});

router.get('/ping', async (ctx) => {
	const host = ctx.query.host;

	if (host === undefined) {
		ctx.redirect('/ping?host=example.com');
		return;
	}

	try {
		// 😈
		const { stdout } = await execp(`ping -c 1 ${host}`);
		ctx.body = `<pre>${stdout}</pre>`;
	} catch ({ stderr }) {
		ctx.body = `<pre>${stderr}</pre>`;
	}
});

app.use(router.allowedMethods());
app.use(router.routes());

app.listen(process.env.PORT || 8000);
