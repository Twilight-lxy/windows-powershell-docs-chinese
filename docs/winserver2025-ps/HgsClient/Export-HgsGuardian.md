---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsClient-help.xml
Module Name: HgsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsclient/export-hgsguardian?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-HgsGuardian
---

# Export-HgsGuardian

## 摘要
导出一个包含公钥的守护者（guardian）。

## 语法

```
Export-HgsGuardian [-InputObject] <CimInstance> [-Path] <String> [<CommonParameters>]
```

## 描述

`Export-HgsGuardian` cmdlet 将包含公钥的守护程序（guardian）导出到一个 `.xml` 文件中。

## 示例

#### 示例 1：导出一个守护者（Guardian）

```powershell
Get-HgsGuardian -Name 'Guardian11' |
    Export-HGsGuardian -Path 'C:\LocalHGSFiles\Guardian11.xml'
```

这个命令使用 `Get-HgsGuardian` cmdlet 来获取名为 `Guardian11` 的守护程序，然后通过管道运算符将该对象传递给当前的 cmdlet。该 cmdlet 会将守护程序导出到指定的文件中。

## 参数

### -InputObject

指定该 cmdlet 的输入参数。

你可以使用这个参数，也可以将输入内容通过管道传递给这个cmdlet。

```yaml
Type: Microsoft.Management.Infrastructure.CimInstance
Parameter Sets: (All)
Aliases: Guardian

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Path

指定用于写入守护者（guardian）的XML表示形式的文件的路径。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: FilePath

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-HgsGuardian](./Get-HgsGuardian.md)

[Import-HgsGuardian](./Import-HgsGuardian.md)

[New-HgsGuardian](./New-HgsGuardian.md)

[Remove-HgsGuardian](./Remove-HgsGuardian.md)
