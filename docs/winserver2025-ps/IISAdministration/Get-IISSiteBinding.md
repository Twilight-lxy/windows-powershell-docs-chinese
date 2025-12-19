---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
online version: https://learn.microsoft.com/powershell/module/iisadministration/get-iissitebinding?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IISSiteBinding
---

# 获取 IISSite 绑定信息

## 摘要
获取指定 IIS 站点上的绑定信息。此 cmdlet 是从 IISAdministration 模块的 1.1.0.0 版本开始引入的。

## 语法

```
Get-IISSiteBinding [-Name] <String> [[-BindingInformation] <String>] [[-Protocol] <String>]
 [<CommonParameters>]
```

## 描述
`Get-IISSiteBinding` cmdlet 可以获取有关网站绑定（website bindings）及其当前状态的其他关键信息。

## 示例

### 示例 1：获取有关 IIS 网站绑定的信息
```
PS C:\> Get-IISSiteBinding "Default Web Site" "*:80:"
```

这个命令用于获取默认网站（Default Web Site）中“*:80:”绑定相关的信息。

### 示例 2：获取有关 IIS 网站所有绑定信息的内容
```
PS C:\> Get-IISSiteBinding "Default Web Site"

protocol bindingInformation sslFlags
-------- ------------------ --------
http     *:80:                  None
http     *:1234:                None
```

这条命令会获取关于“默认网站”（Default Web Site）所有绑定设置的所有配置信息。

## 参数

### -BindingInformation
指定用于新站点的绑定信息字符串。绑定信息的格式为 IP:Port:hostname（例如 192.168.0.1:80:www.contoso.com），其中某个或多个字段可以留空，这相当于使用了通配符（如 *:443:）。在这种表示法中，* 表示所有 IP 地址；而通过将相应的字段留空，则表示所有主机名。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
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
用于配置绑定的协议，通常是http、https或ftp。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String


## 输出

### System.Object

## 备注

## 相关链接

[New-IISSiteBinding](./New-IISSiteBinding.md)

[Remove-IISSiteBinding](./Remove-IISSiteBinding.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)
