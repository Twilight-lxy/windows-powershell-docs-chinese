---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
online version: https://learn.microsoft.com/powershell/module/iisadministration/new-iissitebinding?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-IISSiteBinding
---

# 新的IISSiteBinding配置

## 摘要
向现有的网站添加一个新的绑定（binding）。此cmdlet是在IISAdministration模块的1.1.0.0版本中引入的。

## 语法

```
New-IISSiteBinding [-Name] <String> [-BindingInformation] <String> [[-Protocol] <String>]
 [[-CertificateThumbPrint] <String>] [[-SslFlag] <SslFlags>] [[-CertStoreLocation] <String>] [-Force]
 [-Passthru] [<CommonParameters>]
```

## 描述
为现有的网站添加一个新的绑定（binding）。

## 示例

### 示例 1：创建一个新的 HTTP 绑定
```
PS C:\> New-IISSiteBinding -Name "TestSite" -BindingInformation "*:8080:" -Protocol http
```

这个命令会在一个名为TestSite的网站上创建一个新的HTTP绑定，端口号为“8080”。

### 示例 2：创建一个新的 HTTPS 绑定
```
PS C:\> New-IISSiteBinding -Name "TestSite" -BindingInformation "*:443:" -CertificateThumbPrint "D043B153FCEFD5011B9C28E186A60B9F13103363" -CertStoreLocation "Cert:\LocalMachine\Webhosting" -Protocol https
```

此命令使用一个现有的证书为名为 TestSite 的网站创建一个新的 HTTPS 绑定（绑定信息为 “*:443:”），该证书的指纹（thumbprint）为 D043B153FCEFD5011B9C28E186A60B9F13103363，并将其存储在 Cert:\LocalMachine\Webhosting 证书存储中。

### 示例 3：创建一个新的 HTTPS 绑定，并设置 SNI 和 CentralCertStore SSL 标志
```
PS C:\> New-IISSiteBinding -Name "TestSite" "*:443:foo.com" -Protocol https -SslFlag "Sni, CentralCertStore"
```

此命令在名为 TestSite 的网站上创建一个新的 HTTPS 绑定，绑定地址为 “*:443:foo.com”，并设置了 SNI 和 CentralCertStore SSL 标志的相关参数。


### 示例 4：创建一个新的自签名证书，并使用它来添加一个新的 HTTPS 绑定以用于测试目的
```
$password = "string1"  # put your password on string1
$hostName = "localhost"
$port = "443"
$storeLocation = "Cert:\LocalMachine\My"
$certificate = New-SelfSignedCertificate -DnsName $hostName -CertStoreLocation $storeLocation
$thumbPrint = $certificate.Thumbprint
$bindingInformation = "*:" + $port + ":" + $hostName
$certificatePath = ("cert:\localmachine\my\" + $certificate.Thumbprint)
$securedString = ConvertTo-SecureString -String $password -Force -AsPlainText
Export-PfxCertificate -FilePath "C:\temp\temp.pfx" -Cert $certificatePath -Password $securedString
Import-PfxCertificate -FilePath "C:\temp\temp.pfx" -CertStoreLocation "Cert:\LocalMachine\Root" -Password $securedString
New-IISSiteBinding -Name "TestSite" -BindingInformation $bindingInformation -CertificateThumbPrint $thumbPrint -CertStoreLocation $storeLocation -Protocol https
```

这个 PowerShell 脚本示例展示了如何在个人证书存储（Personal Store）中创建一个自签名证书。将该证书导出到系统根证书存储（ROOT Store），以便在本地机器上将其视为受信任的证书；同时，还会为名为 “TestSite” 的网站添加一个新的 HTTPS 绑定，用于测试目的。

## 参数

### -BindingInformation
指定用于新站点的绑定信息字符串。该绑定信息的格式为 IP:Port:hostname（例如：192.168.0.1:80:www.contoso.com），其中的一个或多个字段可以留空，这相当于使用了通配符（如 *:443:）。在这种表示法中，* 表示所有 IP 地址；而通过将相应的字段留空，则表示所有主机名。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CertificateThumbPrint
指定一个证书指纹（certificate thumbprint），该指纹用于添加新的 HTTPS 绑定（HTTPS binding）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CertStoreLocation
指定证书的存储路径，该路径用于添加新的 HTTPS 绑定。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Cert:\LocalMachine\My, Cert:\LocalMachine\WebHosting, My, WebHosting

Required: False
Position: 5
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定 IIS 网站的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Passthru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Protocol
用于配置绑定的协议，通常是 http、https 或 ftp。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SslFlag
指定新绑定对象的 SSL 标志（SSL Flags）。

```yaml
Type: SslFlags
Parameter Sets: (All)
Aliases:
Accepted values: None, Sni, CentralCertStore, DisableHTTP2, DisableOCSPStp, DisableQUIC, DisableTLS13, DisableLegacyTLS

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### Microsoft.WebAdministration.SslFlags

## 输出

### System.Object

## 备注

## 相关链接

[Get-IISSiteBinding](./Get-IISSiteBinding.md)

[Remove-IISSiteBinding](./Remove-IISSiteBinding.md)

[New-IISSite](./New-IISSite.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)
