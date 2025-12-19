---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
online version: https://learn.microsoft.com/powershell/module/iisadministration/remove-iissitebinding?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IISSiteBinding
---

# 移除 IISSiteBinding

## 摘要
从 IIS 网站中删除绑定。此cmdlet是在 IISAdministration 模块的 1.1.0.0 版本中引入的。

## 语法

```
Remove-IISSiteBinding [-Name] <String> [-BindingInformation] <String> [[-Protocol] <String>]
 [-RemoveConfigOnly] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
从 IIS 网站中删除一个绑定（binding）。

## 示例

### 示例 1
```
PS C:\> Remove-IISSiteBinding -Name "TestSite" -BindingInformation "*:8080:"
```

这条命令会从名为“TestSite”的网站中移除“*:8080:”这一绑定信息。

## 参数

### -BindingInformation
指定用于新站点的绑定信息字符串。该绑定信息的格式为 IP:Port:hostname（例如 192.168.0.1:80:www.contoso.com），其中一个或多个字段可以留空；这相当于使用了通配符（如 *:443:）。在这种表示方式中，* 表示所有 IP 地址，而通过将相应的字段留空则表示所有主机名。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
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

### -RemoveConfigOnly
这表示该操作不会删除 SSL 证书信息，只会移除 `applicationhost.config` 文件中的 IIS 绑定配置信息。

如果你想删除一个与其他现有绑定共享SSL证书的HTTPS绑定配置，只需移除相应的IIS绑定配置即可，这样SSL证书信息仍然会保留。这样做是为了确保其他现有的绑定仍能够访问该证书。

如果您要删除的是一个没有证书的绑定（binding），那么这个参数将被忽略。


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

### -Confirm
在运行该cmdlet之前，会提示您确认是否要继续执行操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Get-IISSiteBinding](./Get-IISSiteBinding.md)

[New-IISSiteBinding](./New-IISSiteBinding.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)
