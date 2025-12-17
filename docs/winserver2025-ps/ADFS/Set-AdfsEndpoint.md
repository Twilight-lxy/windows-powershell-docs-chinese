---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsendpoint?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsEndpoint
---

# 设置 AdfsEndpoint

## 摘要
设置 Web 应用程序代理上的端点。

## 语法

### 地址
```
Set-AdfsEndpoint [[-TargetAddressPath] <String>] -Proxy <Boolean> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 目标对象（Target Object）
```
Set-AdfsEndpoint -TargetEndpoint <Endpoint> -Proxy <Boolean> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

请帮我将这段转换为中文：  
**FullUrl**
```
Set-AdfsEndpoint [-TargetFullUrl] <Uri> -Proxy <Boolean> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsEndpoint` cmdlet 用于设置 Web 应用程序代理（Web Application Proxy）上的端点信息。

## 示例

#### 示例 1：设置一个端点
```
PS C:\> Set-AdfsEndpoint -TargetAddressPath "/adfs/services/trust/13/Windows" -Proxy $True
```

这个命令设置了用于代理的 WS-Trust 1.3 终端。

## 参数

### -PassThru
返回一个表示您正在操作的该项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -Proxy
该字段用于指示端点是否在联邦服务器代理上可用。这是端点中唯一可以设置的字段。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetAddressPath
指定端点的地址路径。该 cmdlet 使您指定的端点能够被外部网络访问（即对外部网络可见）。

```yaml
Type: String
Parameter Sets: Address
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetEndpoint
指定该 cmdlet 所修改的终端点（endpoint）。这个值通常是从管道中获取的。

```yaml
Type: Endpoint
Parameter Sets: TargetObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetFullUrl
指定该 cmdlet 所修改的端点的完整 URL。

```yaml
Type: Uri
Parameter Sets: FullUrl
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftIdentityServer.PowerShell.Resources.Endpoint
此cmdlet返回一个类结构，该结构表示一个端点（endpoint）。

## 输出

### 无

## 备注
* This cmdlet has three parameter-sets. You can use the Address, FullUrl, or TargetEndpoint parameter set, over the pipeline, to identify the endpoint. This cmdlet only allows you to modify the Proxy property of the endpoint.

* Endpoints provide access to the federation server functionality of AD FS, such as token issuance and the publishing of federation metadata.
Depending on the type of endpoint, you can enable or disable the endpoint or control whether the endpoint is published to Web Application Proxy.

## 相关链接

[ Disable-AdfsEndpoint](./Disable-AdfsEndpoint.md)

[Enable-AdfsEndpoint](./Enable-Adfs Endpoint.md)

[Get-AdfsEndpoint](./Get-AdfsEndpoint.md)

