---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/new-adfssamlendpoint?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-AdfsSamlEndpoint
---

# 新的 AdfsSamlTerminal 端点

## 摘要
创建一个 SAML 协议端点对象。

## 语法

```
New-AdfsSamlEndpoint -Binding <String> -Protocol <String> -Uri <Uri> [-IsDefault <Boolean>] [-Index <Int32>]
 [-ResponseUri <Uri>] [<CommonParameters>]
```

## 描述
`New-AdfsSamlEndpoint` cmdlet 用于创建一个安全断言标记语言（SAML）协议端点对象。

## 示例

### 示例 1：创建一个 SAML 终点，并将其分配给依赖方
```
PS C:\> $EP = New-AdfsSamlEndpoint -Binding "POST" -Protocol "SAMLAssertionConsumer" -Uri "https://fabrikam.com/saml/ac"
PS C:\> Set-AdfsRelyingPartyTrust -TargetName "My application" -SamlEndpoint $EP
```

第一个命令创建了一个SAML端点，然后将其存储在$EP变量中。

第二个命令使用了 **Set-AdfsRelyingPartyTrust** cmdlet，将存储在 $EP 变量中的端点分配给一个名为 “My Application” 的依赖方信任关系。

## 参数

### -Binding
指定端点的绑定类型。该参数的可接受值为：POST、SOAP、Artifact 和 Redirect。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Artifact, POST, Redirect, SOAP

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Index
指定为此端点定义的索引。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsDefault
表示这是否是特定协议类型的默认端点。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Protocol
用于指定端点处的服务类型。该参数的合法取值为：SAMLSingleSignOn、SAMLArtifactResolution、SAML Logout 和 SAMLAssertionConsumer。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: SAMLArtifactResolution, SAMLAssertionConsumer, SAMLLogout, SAMLSingleSignOn

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResponseUri
指定端点的响应URI。

```yaml
Type: Uri
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Uri
指定此端点的 URI。

```yaml
Type: Uri
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### MicrosoftIdentityServer.PowerShell.Resources.SamlEndpoint
这个cmdlet生成了一个类结构，用于表示SAML端点资源对象。

## 备注
* You can associate this object with a relying party trust or claims provider trust by using the corresponding cmdlets.

## 相关链接

[Get-AdfsClaimsProviderTrust](./Get-AdfsClaimsProviderTrust.md)

[Get-AdfsRelyingPartyTrust](./Get-AdfsRelyingPartyTrust.md)

[Set-AdfsClaimsProviderTrust](./Set-AdfsClaimsProviderTrust.md)

[Set-AdfsRelyingPartyTrust](./Set-AdfsRelyingPartyTrust.md)

[更新 AdfsClaimsProviderTrust](./Update-AdfsClaimsProviderTrust.md)

[更新：依赖于 ADFS 的方的信任关系配置](./Update-AdfsRelyingPartyTrust.md)

