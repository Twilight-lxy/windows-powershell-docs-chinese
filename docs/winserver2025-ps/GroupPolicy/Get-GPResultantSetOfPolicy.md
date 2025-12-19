---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/get-gpresultantsetofpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-GPResultantSetOfPolicy
---

# Get-GPResultantSetOfPolicy

## 摘要

将用户、计算机或两者的RSoP（运行状态概述）信息读写到文件中。

## 语法

```
Get-GPResultantSetOfPolicy [-Computer <String>] [-User <String>] -ReportType <ReportType>
 -Path <String> [<CommonParameters>]
```

## 描述

`Get-GPResultantSetOfPolicy` cmdlet 可以获取用户或计算机的策略结果集（Resultant Set of Policy，简称 RSoP）信息，并将这些信息写入文件中。

## 示例

### 示例 1：为当前会话中运行的默认用户生成一份报告

```powershell
Get-GPResultantSetOfPolicy -ReportType Xml -Path "c:\reports\LocalUserAndComputerReport.xml"
```

```Output
RsopMode        : Logging
Namespace       : \\COMPUTER-02-PC\Root\Rsop\NS2BBE3F29_794F_4EAE_B9DB_0A2310622534
LoggingComputer : COMPUTER-02
LoggingUser     : CONTOSO\someuser
LoggingMode     : UserAndComputer
```

此命令为当前会话中运行的默认用户生成一份报告。该报告以XML格式生成，并被写入指定的文件中。

### 示例 2：为指定的计算机生成报告

```powershell
$params = @{
    ReportType = 'Xml'
    Path       = 'c:\reports\computer-08.xml'
    Computer   = 'computer-08.contso.com'
}
Get-GPResultantSetOfPolicy @params
```

```Output
RsopMode        : Logging
Namespace       : \\computer-08.contoso.com\Root\Rsop\NS643B2E66_8F54_4407_A813_7D47173B0922
LoggingComputer : computer-08.contoso.com
LoggingUser     : CONTOSO\Administrator
LoggingMode     : Computer
```

此命令会为指定的计算机生成一份报告。该计算机是通过其完全限定域名（FQDN）`computer-08.contoso.com`来识别的。报告以`XML`格式生成，并会被写入到指定的文件中。

### 示例 3：为指定的用户生成一份 HTML 格式的报告，并将其保存到指定的文件中

```powershell
$params = @{
    ReportType = 'HTML'
    Path       = 'c:\reports\UserReport.html'
    User       = 'Contoso\PattiFul'
}
Get-GPResultantSetOfPolicy @params
```

```Output
RsopMode        : Logging
Namespace       : \\COMPUTER-02\Root\Rsop\NS78355E76_C754_41B5_8F5E_B61551837A62
LoggingComputer : COMPUTER-02
LoggingUser     : contoso\someuser
LoggingMode     : User
```

该命令为指定的用户 `Contoso\PattiFul` 生成一份报告（格式为 HTML），并将其保存到指定的文件中。

### 示例 4：为指定的计算机和用户生成一份 HTML 格式的报告，并将其保存到指定的文件中

```powershell
$params = @{
    ReportType = 'HTML'
    Path       = 'c:\reports\UserAndComputerReport.xml'
    User       = 'SomeUser'
    Computer   = 'contoso.com\computer-08'
}
Get-GPResultantSetOfPolicy @params
```

```Output
RsopMode        : Logging
Namespace       : \\computer-08\Root\Rsop\NS72116C25_6570_4586_9B79_FC4F71372E57
LoggingComputer : contoso.com\computer-08
LoggingUser     : someuser
LoggingMode     : UserAndComputer
```

此命令为指定的计算机 `contoso.com\computer-08` 和用户 `SomeUser` 生成一份报告，格式为 HTML，并将其保存到指定的文件中。

## 参数

### -Computer

指定要为其生成报告的计算机的名称。您可以使用以下格式之一来指定计算机名称：

- Full computer name (FQDN computer name); for example, computer-01.sales.contoso.com.

- Fully qualified domain name (FQDN)\computer name; for instance, sales.contoso.com\computer-01.

- NetBIOS domain name\computer name; for instance, sales\computer-01.

- Computer name (host name): for instance, computer-01.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path

指定报告文件的路径；例如：`c:\Reports\GpRsopReport.xml`。

您也可以使用**Path**参数的内置别名**FilePath**来引用它。有关更多信息，请参阅[关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportType

指定RSoP报告的格式。您必须选择`Html`（HTML格式）或`Xml`（XML格式）之一。这些选项不区分大小写。

此参数的可接受值为：`Html` 或 `Xml`。

```yaml
Type: ReportType
Parameter Sets: (All)
Aliases:
Accepted values: Xml, Html

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -User

指定要生成报告的用户名称。您可以使用以下格式之一来输入用户名称：

- Fully qualified domain name (FQDN)\user name; for instance, `sales.contoso.com\SomeUser`.

- NetBIOS domain name\user name; for example, `sales\SomeUser`.

- User name: for example, `SomeUser`.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

这个cmdlet不接受任何对象作为输入。

## 输出

### Microsoft GROUPPolicy.GPRsop

此cmdlet返回一个RSoP对象。

## 备注

* This cmdlet provides only the logging results for a specified computer and user. You must use the
  GPMC to generate RSoP modeling information.

## 相关链接

