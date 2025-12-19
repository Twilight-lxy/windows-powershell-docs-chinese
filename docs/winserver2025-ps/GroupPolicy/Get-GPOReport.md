---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/get-gporeport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-GPOReport
---

# Get-GPOReport

## 摘要

为指定的组策略对象（GPO）或域中的所有组策略对象生成报告，报告可以以XML或HTML格式呈现。

## 语法

### 使用 ByGUID（默认值）

```
Get-GPOReport [-Guid] <Guid> [-ReportType] <ReportType> [[-Path] <String>] [[-Domain] <String>]
 [[-Server] <String>] [<CommonParameters>]
```

### 按名称查找

```
Get-GPOReport [-Name] <String> [-ReportType] <ReportType> [[-Path] <String>] [[-Domain] <String>]
 [[-Server] <String>] [<CommonParameters>]
```

### ReportAll

```
Get-GPOReport [-ReportType] <ReportType> [[-Path] <String>] [[-Domain] <String>]
 [[-Server] <String>] [-All] [<CommonParameters>]
```

## 描述

`Get-GPOReport` cmdlet 会生成一份报告，该报告可以是 XML 格式或 HTML 格式，用于描述指定的组策略对象（GPO）或域中所有 GPO 的属性和策略设置。每個 GPO 的报告信息包括：详细信息、链接、安全过滤规则、Windows 管理规范（WMI）过滤规则、委派设置以及计算机和用户配置。

您可以指定 `All` 参数，为域中的每个 GPO 生成报告；或者您也可以指定 `Name` 或 `Guid` 参数，只为单个 GPO 生成报告。此外，您还可以将 GPO 对象传递给此 cmdlet。如果您通过 `Path` 参数指定了一个文件，则报告会写入该文件中；否则，报告会显示在屏幕上。

## 示例

### 示例 1：为指定的 GPO 生成 HTML 报告

```powershell
Get-GPOReport -Name "TestGPO1" -ReportType HTML -Path "C:\GPOReports\GPOReport1.html"
```

此命令为 GPO `TestGPO1` 生成一份 HTML 格式的报告，并将其写入文件 `C:\GPOReports\GPOReport1.html` 中。

### 示例 2：为指定域中的每个 GPO 生成一份 XML 报告

```powershell
$params = @{
    All         = $true
    Domain      = 'sales.contoso.com'
    Server      = 'DC1'
    ReportType  = 'XML'
    Path        = 'C:\GPOReports\GPOReportsAll.xml'
}
Get-GPOReport @params
```

该命令会为 `sales.contoso.com` 域中的每个 GPO 生成一份 XML 格式的报告，并将其写入文件 `C:\GPOReports\GPOReportsAll.xml`。在执行此操作时会与 `DC1` 域控制器进行通信。

如果用户账户的域（或者对于启动和关闭脚本来说，是计算机账户的域）与 `sales.contoso2.com` 不同，则这两个域之间必须存在信任关系。

### 示例 3：为具有指定 GUID 的 GPO 生成 XML 报告

```powershell
Get-GPOReport -GUID 73624cc9-e8f2-4f05-8802-193fae8773ce -ReportType XML
```

该命令会为具有指定GUID的GPO生成一份XML格式的报告。由于没有提供**路径（Path）**参数，因此报告会被直接显示在屏幕上。

## 参数

### -All

表示该cmdlet会为域中的所有GPO生成报告。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ReportAll
Aliases:

Required: True
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Domain

指定此 cmdlet 所适用的域。必须提供该域的完全限定域名（FQDN）。

关于 `Get-GPOReport` cmdlet：

- If a single GPO is specified, it must exist in this domain.

- If the **All** parameter is specified, a report is generated for each GPO in this domain.

如果您没有指定 **Domain** 参数，那么将使用当前会话所运行用户的域信息。如果该cmdlet是从计算机启动或关闭脚本中执行的，则会使用计算机的域信息。有关更多详细信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域名与当前会话的运行用户的域名不同，或者（对于启动或关闭脚本来说）是与计算机相关的域名不同，那么该域名与用户或计算机的域名之间必须存在信任关系。

您也可以使用该域的内置别名 **DomainName** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell/core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DomainName

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Guid

通过全局唯一标识符（GUID）指定要生成报告的组策略对象（GPO）。该 GUID 可唯一地识别该 GPO。

您也可以使用**Guid**参数的内置别名**Id**来引用它。有关更多信息，请参阅[关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: Guid
Parameter Sets: ByGUID
Aliases: Id

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name

根据显示名称指定要生成报告的组策略对象（GPO）。

显示名称在域中并不保证是唯一的。如果域中存在另一个具有相同显示名称的GPO，将会出现错误。你可以使用**Guid**参数来唯一标识一个GPO。

您也可以通过其内置别名 **DisplayName** 来引用 **Name** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: ByName
Aliases: DisplayName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Path

指定报告文件的路径；例如：`c:\Reports\GpoReport.xml`。如果没有指定路径，则报告会直接显示在屏幕上。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportType

指定报告的格式。您必须选择Html（用于HTML格式）或Xml（用于XML格式）。这些值不区分大小写。

对于这种对象类型，允许使用以下值。

```yaml
Type: ReportType
Parameter Sets: (All)
Aliases:
Accepted values: Xml, Html

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server

指定此 cmdlet 用于联系以完成操作的域控制器的名称。您可以指定完全合格的域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统将会联系主域控制器（Primary Domain Controller，简称 PDC）的模拟器。

您可以使用这个参数的内置别名 **DC** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DC

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft(GroupPolicy.Gpo)

一个用于表示组策略对象（GPO）的实体。不支持包含来自不同域的GPO的集合。

## 输出

### 无

这个cmdlet不会生成任何输出。

## 备注

* You can use the **Domain** parameter to explicitly specify the domain for this cmdlet.

如果您没有明确指定域名，该cmdlet会使用默认域名。默认域名是指当前会话所运行的安全上下文用于访问网络资源时所使用的域名。这个域名通常就是运行该会话的用户的域名；例如，通过“程序文件”菜单打开Windows PowerShell来启动会话的用户的域名，或者在“runas”命令中指定的用户的域名。不过，计算机启动和关闭脚本是在LocalSystem账户的上下文中运行的。LocalSystem账户是一个内置的本地账户，它以计算机账户的权限来访问网络资源。因此，当从这个启动或关闭脚本中运行该cmdlet时，默认域名就是计算机所属的域名称。

此 cmdlet 的一个实例只能使用一个域。如果您将一组 GPO（Microsoft.GroupPolicy.Gpo）对象通过管道传递给此 cmdlet，那么集合中第一个 GPO 对象的 **DomainName** 属性将指定该 cmdlet 使用的域。这是因为 **DomainName** 是 **Domain** 参数的内置别名，而 **Domain** 参数可以从管道中通过属性名称获取其值。如果集合中的某个 GPO 不属于该域，则会引发一个无法终止的错误。如果该域与用户账户、启动/关闭脚本或计算机账户所在的域不同，那么这两个域之间必须存在信任关系。

## 相关链接
