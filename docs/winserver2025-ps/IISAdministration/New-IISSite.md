---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/new-iissite?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-IISSite
---

# 新版IISS网站

## 摘要
创建一个 IIS 网站。

## 语法

```
New-IISSite [-Name] <String> [-PhysicalPath] <String> [-BindingInformation] <String> [[-Protocol] <String>]
 [[-CertificateThumbPrint] <String>] [[-SslFlag] <SslFlags>] [[-CertStoreLocation] <String>] [-Force]
 [-Passthru] [<CommonParameters>]
```

## 描述
`New-IISSite` cmdlet 用于创建一个互联网信息服务（IIS）网站，该网站的根目录设置为指定的物理站点，并配置监听特定 IP 地址、端口号以及主机名的绑定信息。

## 示例

### 示例 1：添加一个新的 IIS 网站
```
PS C:\> New-IISSite -Name "TestSite" -BindingInformation "*:8080:" -PhysicalPath "$env:systemdrive\inetpub\testsite"
```

这个命令创建了一个名为 TestSite 的新网站。

### 示例 2：添加一个新的网站，并将该网站默认应用程序的应用程序池设置为自定义名称
```
PS C:\> Start-IISCommitDelay
PS C:\> $TestSite = New-IISSite -Name TestSite -BindingInformation "*:8080:" -PhysicalPath "$env:systemdrive\inetpub\testsite" -Passthru
PS C:\> $TestSite.Applications["/"].ApplicationPoolName = "TestSiteAppPool"
PS C:\> Stop-IISCommitDelay
```

这个命令创建了一个名为 TestSite 的网站，并将默认应用程序分配给 TestSiteAppPool 应用程序池。

### 示例 3：添加一个支持 HTTPS 协议的新网站
```
PS C:\> New-IISSite -Name "TestSite" -PhysicalPath "$env:systemdrive\inetpub\testsite" -BindingInformation "*:443:" -CertificateThumbPrint "D043B153FCEFD5011B9C28E186A60B9F13103363" -CertStoreLocation "Cert:\LocalMachine\Webhosting" -Protocol https
```

这个命令会创建一个名为“TestSite”的网站，并为其配置HTTPS绑定。

## 参数

### -BindingInformation
指定用于新站点的绑定信息字符串。该绑定信息的格式为 IP:Port:hostname（例如 192.168.0.1:80:www.contoso.com），其中某个或多个字段可以留空；这相当于使用了通配符（如 *:443:）。在这种情况下，* 表示所有 IP 地址；而通过将相应字段留空，则表示所有主机名。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
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
Position: Named
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
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需请求用户确认。

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
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Passthru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -PhysicalPath
指定新的 IIS 网站的物理路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Protocol
用于配置绑定的协议，通常是http、https或ftp。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SslFlag
指定新绑定的SSL标志设置。

```yaml
Type: SslFlags
Parameter Sets: (All)
Aliases:
Accepted values: None, Sni, CentralCertStore, DisableHTTP2, DisableOCSPStp, DisableQUIC, DisableTLS13, DisableLegacyTLS

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### System.String

### Microsoft.Web ADMINISTRATION.SslFlags

## 输出

### System.Object

## 备注

## 相关链接

[获取 IISSite](./Get-IISSite.md)

[Remove-IISSite](./Remove-IISSite.md)

[启动 IISS 站点](./Start-IISSite.md)

[停止使用 IISS 网站](./Stop-IISSite.md)

[New-IISSiteBinding](./New-IISSiteBinding.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

